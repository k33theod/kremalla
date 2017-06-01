def kremmala():
  leksi=import_word()
  grammata=[]
  lathi=0
  print_leksi(leksi,grammata)
  while lathi<5 and (not leksi_in_grammata(leksi,grammata)):
    gramma = input ("Δώσε γράμμα : ")
    if gramma not in grammata:
      grammata.append(gramma)
      if gramma not in leksi:
        lathi+=1
      else:
        print_leksi(leksi,grammata)
    else: 
      print("Το γρράμμα το έχεις ξαναδώσει δώσε άλλο")
    
    if leksi_in_grammata(leksi,grammata):
      print("Sigxaritiria brikes ti leji")
      
    if lathi==5:
      print("Exases ekanes 5 lathi")
      
      
def import_word():
	return input ("Δωσε τη λέξη για να παίξουμε : ")
	 
def print_leksi(leksi,grammata):
  for gramma in leksi:
    if gramma in grammata:
      print(gramma+' ', end='')
    else:
      print('_ ', end='')
  print('\n')
      
def leksi_in_grammata(leksi,grammata):
  for i in leksi:
    if i not in grammata:
      return False
  return True
