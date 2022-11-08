import requests

mais = "s"

def format_list():
  for i in range(len(sites)):
    sites[i] = sites[i].strip()
    sites[i] = sites[i].lower()
    if "http://" not in sites[i] and "." in sites[i]:
      sites[i] = "http://"+ sites[i]

def on_off():
  for i in range(len(sites)):
    if "." not in sites[i]:
        print(f"{sites[i]} URL inválida.")
    else:
      try:
        r = requests.get(sites[i]) 
        check = r.status_code
        if check == 200: 
          print(f"{sites[i]} Site online!")
      except:
        print(f"{sites[i]} Site offline!") 
     
while mais == "S" or mais == "s":
  print("Bem-vindo ao Verificador de Sites 1.0!")
  print("Insira as URLs dos sites que deseja verificar o status. (separadas por vírgula)\n")
  sites = input()
  sites = sites.split(",")
  format_list()
  on_off()
   
  mais = input('Precisa verificar mais algum site? s/n ')
  while mais != "N" and mais != "n" and mais != "S" and mais != "s":
    print("Opção invalida.")
    mais = input('Precisa verificar mais algum site? s/n ')
  if mais == "N" or mais == "n":
    print("Programa finalizado com sucesso")
    break