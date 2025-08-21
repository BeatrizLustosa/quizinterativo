import os

op = input("Digite (1) para lustosa.b19@gmail.com ou (2) para emanuelycarvalhoniza@gmail.com: ")
if(op == "1"):
    email = "lustosa.b19@gmail.com"
else:
    email = "emanuelycarvalhoniza@gmail.com"

msg_commit = ""
while(len(msg_commit)<10):
    msg_commit = input("Mensagem do commit (maior que 10 caracateres): ")

print("\n\nConfigurando email...")
comando = f"git config user.email \"{email}\""
os.system(comando)

print("\nAdicionando mudanças e realizando commit...")
comando = "git add *"
os.system(comando)
comando = f"git commit -m \"{msg_commit}\""
os.system(comando)

print("\nEnviando ao GitHub. Abra a outra janela para se autenticar...")
comando = "git push"
os.system(comando)

print("\nEnvio realizado com sucesso...")
