from flask import Flask, render_template, request
import boto3

app = Flask(__name__)

# 1. Configuración de AWS
S3_BUCKET = "cloudgallery-bucket-12345"
s3 = boto3.client("s3")

# 2. Definición de Rutas
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if 'file' not in request.files:
        return "No hay archivo" # <--- Esta línea debe tener más espacios que el 'if'
    
    file = request.files["file"]
    try:
        s3.upload_fileobj(file, S3_BUCKET, file.filename)
        return "Archivo subido con éxito"
    except Exception as e:
        return f"Error: {str(e)}"


# 3. Arranque (En CloudShell usa el puerto 8080)
if __name__ == "__main__":
 app.run(host='0.0.0.0', port=8080)