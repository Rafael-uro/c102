import os ;
import shutil;

from_dir = r"C:\Users\Suiene.Uró\Downloads"


to_dir = r"C:\Users\Suiene.Uró\arquivos"


listfiles = os.listdir(from_dir)


for file in listfiles:
    name, extesion = os.path.splitext(file)
    print(name)
    print(extesion)

    if (extesion == ""):
        continue
 
    if (extesion in [".txt", ".doc", ".docx",".pdf"]):
        path1 = from_dir + "/" + file
        path2 = to_dir + "/" + "arquivos e documentos"
        path3 = to_dir + "/" + "arquivos e documentos" + "/" + file

        if(os.path.exists(path2)):
            print("Movendo arquivo")
            shutil.move(path1, path3)

        else:
            os.makedirs(path2)    
            print("criando a pasta")
            shutil.move(path1, path3)