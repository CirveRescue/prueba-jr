from app import create_app

# Creramos la aplicación Flask
app = create_app()
# Configuramos el puerto y el modo de depuración
if __name__ == '__main__':
    app.run(port=5000, debug=True)