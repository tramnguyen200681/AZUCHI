from flask import Flask, request, jsonify 
from flask_cors import CORS

#request: retrieve data from client
#jsonify: return the result to FE in JSON
#import CORS: Allow FE and BE are in different locations (localhost 5500 and 5000...)

app = Flask(__name__)
CORS(app)

users = [] # Each user is a dict {'username': 'abc'}

#Connect database:
def get_db_connection():
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()

#Create API at /register and only allow POST (send data from form)
#Create API at /login andFE send login info


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')


    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    existing_user = cursor.fetchone()


    if existing_user:
        conn.close()
        return jsonify({"success": False, "message": "Tài khoản đã tồn tại."})
    
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

    return jsonify({"success": True, "message": "Đăng ký thành công."})

   # for u in users:
    #    if u['username'] == username:
     #       return jsonify({"success": False, "message": "Tài khoản đã tồn tại."})
        
#    users.append({'username': username, 'password': password})
 #   return jsonify({"success": True, "message": "Đăng ký thành công."})
    
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        return jsonify({"success": True, "message": "Đăng nhập thành công."})
    else:
        return jsonify({"success": False, "message": "Sai tài khoản hoặc mật khẩu."})



  #  for u in users:
   #     if u['username'] == username and u['password'] == password:
    #        return jsonify({"success": True, "message": "Đăng nhập thành công."})
     #   
      #  return jsonify({"success": False, "message": "Sai tài khoản hoặc mật khẩu."})
    

if __name__ == '__main__':
    app.run(debug=True)