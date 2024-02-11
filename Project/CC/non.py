from flask import Flask, jsonify, request
from flask_cors import CORS  # Import CORS
from flask import Flask, render_template
import json


import sqlite3
import datetime

app = Flask(__name__)
CORS(app)

# app.config['JSONIFY_MIMETYPE'] = 'application/json'

@app.route('/checkOk',methods=['GET'])
def getCheckOk():
    return "Ok"

# Endpoint to fetch data from the database
@app.route('/data', methods=['GET'])
def get_data():
    conn = sqlite3.connect('/Users/matikahunbumrung/Desktop/PloyRBL/projectRBL/Project/SQL/mydatabase.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mytable")  # Replace 'your_table_name' with your actual table name
    rows = cursor.fetchall()
    conn.close()

    data_list = []
    for row in rows:
        data_dict = {
            'id': row[0],  # Assuming the first column is the ID
            'column1': row[1],  # Replace with your column names
            'column2': row[2],  # Replace with your column names
            'column3': row[3],
            'column4': row[4],
            'column5': row[5],
            'column6': row[6],
            # Add more columns as needed
        }
        data_list.append(data_dict)

    return jsonify({'data': data_list})

@app.route('/log', methods=['GET'])
def getLog():
    conn = sqlite3.connect('/Users/matikahunbumrung/Desktop/PloyRBL/projectRBL/Project/SQL/mydatabase.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Log")  # Replace 'your_table_name' with your actual table name
    rows = cursor.fetchall()
    conn.close()

    data_list = []
    for row in rows:
        data_dict = {
            'id': row[0],  # Assuming the first column is the ID
            'column1': row[1],  # Replace with your column names
            'column2': row[2],  # Replace with your column names
            # Add more columns as needed
        }
        data_list.append(data_dict)

    return jsonify({'data': data_list})

    
# ==================== Noted ====================
# @app.route('/saveDate', methods=['POST'])
# def saveDate():
#     try:
#         date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         name = request.form.get('name')  # ใช้ request.form.get แทน request.args.post
#         card = request.form.get('card')
#         print(name)
#         conn = sqlite3.connect('/Users/matikahunbumrung/Desktop/PloyRBL/Project/SQL/mydatabase.db')

#         cursor = conn.cursor()
#         cursor.execute('INSERT INTO Log (Date, Name,Card) VALUES (?, ?,?)', (date, name,card))
#         conn.commit()
#         conn.close()

#         return jsonify({'message': 'Data inserted successfully.'}), 201
#     except Exception as e:
#         print("Error:", str(e))
#         return jsonify({'error': str(e)}), 500



# @app.route('/saveData', methods=['POST'])
# def save_data():
#     try:
#         date = datetime.datetime.now().strftime("%Y-%m-%d")
#         data = request.json
#         name = data.get('name')
#         card = data.get('card')
#         conn = sqlite3.connect('/Users/matikahunbumrung/Desktop/Project/SQL/mydatabase.db')
#         cursor = conn.cursor()
#         cursor.execute('INSERT INTO Log (Date, Name, Card) VALUES (?, ?, ?)', (date, name, card))
#         conn.commit()
#         conn.close()

#         return jsonify({'message': 'Data inserted successfully.'}), 201
#     except Exception as e:
#         print("Error:", str(e))
#         return jsonify({'error': str(e)}), 500

# ================================================================================


    
@app.route('/saveData', methods=['POST'])
def save_data():
    try:
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        data = request.json
        name = data.get('name').split(",")[0].split(":")[1]
        course = data.get('name').split(",")[1].split(":")[1]
        # card = data.get('card')
        conn = sqlite3.connect('/Users/matikahunbumrung/Desktop/PloyRBL/projectRBL/Project/SQL/mydatabase.db')
        cursor = conn.cursor()

        # Check if the data already exists in the database
        cursor.execute('SELECT * FROM Log WHERE nickname = ? OR cours = ?', (name, course))
        existing_data = cursor.fetchall()

        if existing_data:
            # If data already exists, delete all existing data and insert new data
            cursor.execute('DELETE FROM Log WHERE nickname = ? OR cours = ?', (name, course))


        cursor.execute('INSERT INTO Log (Date, nickname, cours) VALUES (?, ?, ?)', (date, name, course))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Data inserted successfully.'}), 201
    except Exception as e:
        print("Error:", str(e))
        return jsonify({'error': str(e)}), 500
    




@app.route('/testSave',methods=['POST'])
def testSave():
    data1 = request.args.get('test')
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # cardID = request.args.get('cardID')
    response_data = {'data1': data1, 'data2': date}

    conn = sqlite3.connect('/Users/matikahunbumrung/Desktop/PloyRBL/projectRBL/Project/SQL/mydatabase.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Log (Date, Name) VALUES (?, ?)', (date, data1))
    conn.commit()
    conn.close()


    return jsonify(response_data), 200


@app.route('/testCount', methods=['GET'])
def testCount():
    try:
        conn = sqlite3.connect('/Users/matikahunbumrung/Desktop/PloyRBL/projectRBL/Project/SQL/mydatabase.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM mytable WHERE name = 'ploy'")
        data = cursor.fetchall()
        conn.close()

        if data:
            data_list = []
            for row in data:
                data_dict = {
                    'id': row[0],  # Assuming the first column is the ID
                    'column1': row[1],  # Replace with your column names
                    'column2': row[2],  # Replace with your column names
                    'column3': row[3],
                    # Add more columns as needed
                }
                data_list.append(data_dict)
            print(f'Count : {len(data_list)}')
            count = f'Count : {len(data_list)}'

            
            return jsonify({'data': data_list}) 
        else:
            return jsonify({'message': 'No data found for the specified condition'})

    except Exception as e:
        return jsonify({'error': str(e)})


    

if __name__ == '__main__':
    ip = '192.168.3.13'
    # ip = '172.20.10.5'
    # app.run(debug=True,host='172.20.10.4',port=5000)
    app.run(debug=True,host=ip,port=8000)
    # app.run(debug=True)



