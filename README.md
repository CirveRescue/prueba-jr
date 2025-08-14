# API de Chistes de Chuck Norris 🥋

Este es un mini proyecto en **Python + Flask** que sirve como “puente” para la [API pública de Chuck Norris](https://api.chucknorris.io/).

La idea es simple: desde aquí puedes pedir las categorías de chistes disponibles y sacar un chiste aleatorio de la categoría que quieras.

---

## 🔧 Qué necesitas antes de empezar

* **Python 3.8 o superior**
* `pip` para instalar dependencias

---

## 🚀 Cómo ponerlo a correr

1. **Clona este repo** (o crea la misma estructura de archivos en tu compu):

   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio
   ```

2. **Instala las dependencias**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Arranca el servidor**:

   ```bash
   python run.py
   ```

   Si todo va bien, tu API estará viva en:

   ```
   http://127.0.0.1:5000
   ```

---

## 📌 Endpoints que puedes usar

### 1️⃣ Ver todas las categorías

* **Método:** `GET`
* **URL:** `/categories`
* **Ejemplo:**

  ```bash
  curl http://127.0.0.1:5000/categories
  ```
* **Respuesta:**

  ```json
  [
      "animal",
      "career",
      "celebrity",
      "dev",
      "explicit",
      "fashion",
      "food",
      "history",
      "money",
      "movie",
      "music",
      "political",
      "religion",
      "science",
      "sport",
      "travel"
  ]
  ```

---

### 2️⃣ Sacar un chiste random por categoría

* **Método:** `GET`

* **URL:** `/joke/{nombre-de-la-categoria}`

* **Ejemplo:**

  ```bash
  curl http://127.0.0.1:5000/joke/dev
  ```

* **Respuesta:**

  ```json
  {
    "id": "pwn69x3otd2yqehdsohbfg",
    "url": "https://api.chucknorris.io/jokes/pwn69x3otd2yqehdsohbfg",
    "Categoria": "dev",
    "Broma": "Chuck Norris's keyboard doesn't have a F1 key, the computer asks him for help."
  }
  ```

* **Si pides una categoría que no existe** (ejemplo “programacion”):

  ```bash
  curl -i http://127.0.0.1:5000/joke/programacion
  ```

  ```json
  {
    "error": "La categoría 'programacion' no es válida."
  }
  ```

