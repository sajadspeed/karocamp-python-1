import sqlite3

class Field:
    def __init__(self, required=True):
        self.required = required

    def validate(self, value):
        if self.required and (value is None or str(value).strip() == ""):
            raise ValueError("This field is required.")
        return value

class StringField(Field):
    def __init__(self, required=True, min_length=0):
        super().__init__(required)
        self.min_length = min_length

    def validate(self, value):
        value = super().validate(value)
        if value is not None:
            if not isinstance(value, str):
                value = str(value)
            if len(value) < self.min_length:
                raise ValueError(f"Must be at least {self.min_length} characters long.")
        return value

class IntegerField(Field):
    def __init__(self, required=True, min_value=None):
        super().__init__(required)
        self.min_value = min_value

    def validate(self, value):
        if self.required and (value is None or str(value).strip() == ""):
            raise ValueError("This field is required.")
        if value is not None and str(value).strip() != "":
            try:
                val = int(value)
            except (ValueError, TypeError):
                raise ValueError("Must be a valid integer.")
            if self.min_value is not None and val < self.min_value:
                raise ValueError(f"Must be greater than or equal to {self.min_value}.")
            return val
        return None

class ModelMeta(type):
    def __new__(mcs, name, bases, attrs):
        fields = {}
        for key, value in list(attrs.items()):
            if isinstance(value, Field):
                fields[key] = value
                attrs.pop(key)
        attrs['_fields'] = fields
        return super().__new__(mcs, name, bases, attrs)

class Model(metaclass=ModelMeta):
    db_path = "university.db"
    table_name = ""

    def __init__(self, **kwargs):
        self.errors = {}
        for key, field in self._fields.items():
            value = kwargs.get(key, None)
            try:
                validated_value = field.validate(value)
                setattr(self, key, validated_value)
            except ValueError as e:
                self.errors[key] = str(e)
                setattr(self, key, value)

        # Keep extra attributes like id if present
        if 'id' in kwargs:
            self.id = kwargs['id']

    @classmethod
    def get_db(cls):
        conn = sqlite3.connect(cls.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    @classmethod
    def all(cls):
        conn = cls.get_db()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {cls.table_name}")
        rows = cursor.fetchall()
        conn.close()
        return [cls(**dict(row)) for row in rows]

    @classmethod
    def find(cls, record_id):
        conn = cls.get_db()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {cls.table_name} WHERE id = ?", (record_id,))
        row = cursor.fetchone()
        conn.close()
        return cls(**dict(row)) if row else None

    def save(self):
        # Validate all fields before saving
        self.errors = {}
        for key, field in self._fields.items():
            value = getattr(self, key, None)
            try:
                validated_value = field.validate(value)
                setattr(self, key, validated_value)
            except ValueError as e:
                self.errors[key] = str(e)

        if self.errors:
            raise ValueError("Validation failed.")

        conn = self.get_db()
        cursor = conn.cursor()

        attributes = {k: v for k, v in self.__dict__.items() if k in self._fields}

        if hasattr(self, 'id') and self.id:
            keys = [f"{k} = ?" for k in attributes.keys()]
            values = list(attributes.values())
            values.append(self.id)
            query = f"UPDATE {self.table_name} SET {', '.join(keys)} WHERE id = ?"
            cursor.execute(query, values)
        else:
            keys = attributes.keys()
            values = list(attributes.values())
            placeholders = ['?'] * len(keys)
            query = f"INSERT INTO {self.table_name} ({', '.join(keys)}) VALUES ({', '.join(placeholders)})"
            cursor.execute(query, values)
            self.id = cursor.lastrowid

        conn.commit()
        conn.close()
        return self

    def delete(self):
        if hasattr(self, 'id') and self.id:
            conn = self.get_db()
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM {self.table_name} WHERE id = ?", (self.id,))
            conn.commit()
            conn.close()
