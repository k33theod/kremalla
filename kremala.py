import random
words=('κιθαρα','τραπεζι','παπουτσι', 'αγγουρι', 'ρολοι', 'κουπα', 'οπτασια', 'οθονη', 'χιονι',
'πατατα', 'ραδιο', 'οπλο', 'μπαλα', 'μπορα' , 'αγκυρα', 'πλοιο', 'μανικι', 'παλουκι','τσιχλα',
'ριζα','ρυζι','κρικος','οραμα','λαμψη', 'αστρο','ουρανος')

def kremmala():
  leksi=random.choice(words)
  grammata=[]
  lathi=0
  print(f'Λέξη με {len(leksi)} γράμματα')
  print_leksi(leksi,grammata)
  
  while lathi<5 and (not leksi_in_grammata(leksi,grammata)):
    gramma = input ("Δώσε γράμμα : ")
    if gramma not in grammata:
      grammata.append(gramma)
      if gramma not in leksi:
        lathi+=1
        print(f"Έχεις {lathi} από 5 λάθη")
      else:
        print_leksi(leksi,grammata)
    else: 
      print("Το γράμμα το έχεις ξαναδώσει δώσε άλλο")
    
    if leksi_in_grammata(leksi,grammata):
      print(f"Συγχαρητήρια βρήκες τη λέξη '{leksi}'")
      
    if lathi==5:
      print("Έχασες έκανες 5 λάθη")
      print(f"Η λέξη ήταν '{leksi}'")
  play_again=input("Θέλεις να παίξεις ξανά (ναι/όχι): ")
  if play_again=='ναι':
    kremmala()
      
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
kremmala()
