#első feleadat 9dk
IDEI_ÉV = 2022
print(type(IDEI_ÉV))
print( 'Az idei év :',IDEI_ÉV, sep=',,,>')
felhasználó_kora = input('hány éves vagy?')
print(type(felhasználó_kora))
print('Te most', felhasználó_kora,'éves vagy.')
felhasználó_kora = int(felhasználó_kora)
születési_év = IDEI_ÉV - felhasználó_kora
print('Ekkor születtél:', születési_év,'.', sep='')
