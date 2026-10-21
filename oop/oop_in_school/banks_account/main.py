from banks import BlueBank, TegaratBank
from reports import ReportTextFile, ReportPrint, ReportSMS

reporter_file = ReportTextFile("./reports.txt")
report_print = ReportPrint()
report_sms = ReportSMS()

danial_account = BlueBank("Dnial", 20, reporters=[reporter_file, report_sms])
sajad_account = BlueBank("Sajad", 6, masdoodi=False, reporters=[report_print])
paria_account = TegaratBank(
    "Paria", 100, reporters=[report_print, report_sms, reporter_file]
)

print(danial_account + sajad_account)

quit()

danial_account.kart_be_kart(sajad_account, 18)

paria_account.kart_be_kart(sajad_account, 50)

# print(result)

danial_account.show_mojoodi()
sajad_account.show_mojoodi()
