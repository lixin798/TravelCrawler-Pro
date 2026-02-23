from datetime import datetime

from flask import request, jsonify  # 新增 request 和 jsonify
from flask import Flask, render_template
import pymysql

app = Flask(__name__)

# 数据库连接配置
def connect_db():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='123456',
        database='travel_project',
        charset='utf8mb4'
    )

# 创建表
def create_tables():
    conn = connect_db()
    cursor = conn.cursor()
    create_hotel_table = """
    CREATE TABLE IF NOT EXISTS hotel_reservations (
        id INT AUTO_INCREMENT PRIMARY KEY,
        hotel_name VARCHAR(255) NOT NULL,
        check_in_date DATE NOT NULL,
        check_out_date DATE NOT NULL,
        room_type VARCHAR(255) NOT NULL,
        appointment_category VARCHAR(255),
        numbering VARCHAR(255),
        operation VARCHAR(255)
    )
    """
    create_flight_table = """
    CREATE TABLE IF NOT EXISTS flight_reservations (
        id INT AUTO_INCREMENT PRIMARY KEY,
        place_of_departure VARCHAR(255) NOT NULL,
        destinations VARCHAR(255) NOT NULL,
        departure_date DATETIME NOT NULL, -- 修改为DATETIME类型
        flight_type VARCHAR(255) NOT NULL,
        appointment_category VARCHAR(255),
        numbering VARCHAR(255),
        operation VARCHAR(255)
    )
    """
    create_package_table = """
    CREATE TABLE IF NOT EXISTS package_reservations (
        id INT AUTO_INCREMENT PRIMARY KEY,
        destinations VARCHAR(255) NOT NULL,
        travel_dates DATE NOT NULL,
        number_of_people INT NOT NULL,
        package_type VARCHAR(255) NOT NULL,
        appointment_category VARCHAR(255),
        numbering VARCHAR(255),
        operation VARCHAR(255)
    )
    """
    cursor.execute(create_hotel_table)
    cursor.execute(create_flight_table)
    cursor.execute(create_package_table)
    conn.commit()
    cursor.close()
    conn.close()


# 主页路由
@app.route('/')
def index():
    return render_template('index.html', now=datetime.now())

# 注册页面路由
@app.route('/register')
def register():
    return render_template('Registration_Page.html')

# 登录页面路由
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/chongqing')
def chongqing():
    return render_template('chongqing.html')

@app.route('/shanghai')
def shanghai():
    return render_template('shanghai.html')

@app.route('/guangzhou')
def guangzhou():
    return render_template('guangzhou.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')
@app.route('/privacy')
def privacy():
    return render_template('privacy.html')
@app.route('/terms')
def terms():
    return render_template('terms.html')
@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

# 新增攻略列表路由
@app.route('/travel_guides')
def travel_guides():
    # 模拟攻略数据（实际需从数据库查询）
    guides = [
        {
            "id": 1,
            "title": "中国旅行必备物品清单",
            "category": "旅行准备",
            "category_color": "primary",  # 对应主页蓝色
            "description": "了解去中国旅行需要准备的重要物品，包括证件、衣物、电子设备等实用建议。",
            "image_url": "https://picsum.photos/id/1039/800/600",
            "publish_date": "2023-05-15",
            "views": "2,345"
        },
        {
            "id": 2,
            "title": "中国必尝的十大美食",
            "category": "美食推荐",
            "category_color": "secondary",  # 对应主页橙色
            "description": "从北京烤鸭到四川火锅，从上海小笼包到广东早茶，带您领略中国各地的美食文化。",
            "image_url": "https://picsum.photos/id/1040/800/600",
            "publish_date": "2023-06-20",
            "views": "3,127"
        },
        {
            "id": 3,
            "title": "体验中国传统文化活动",
            "category": "文化体验",
            "category_color": "green-500",  # 新增绿色类别
            "description": "参与中国传统手工艺制作、学习书法绘画、观看京剧表演，深入体验中国文化魅力。",
            "image_url": "https://picsum.photos/id/1041/800/600",
            "publish_date": "2023-07-10",
            "views": "1,892"
        }
    ]
    return render_template('all_travel_guides.html', guides=guides)

# 新增 guide_detail 路由
@app.route('/guide_detail/<int:guide_id>')
def guide_detail(guide_id):
    # 这里可以根据 guide_id 从数据库中查询具体的攻略信息
    # 暂时使用模拟数据
    guides = [
        {
            "id": 1,
            "title": "中国旅行必备物品清单",
            "category": "旅行准备",
            "category_color": "primary",  # 对应主页蓝色
            "description": "了解去中国旅行需要准备的重要物品，包括证件、衣物、电子设备等实用建议。",
            "image_url": "https://picsum.photos/id/1039/800/600",
            "publish_date": "2023-05-15",
            "views": "2,345"
        },
        {
            "id": 2,
            "title": "中国必尝的十大美食",
            "category": "美食推荐",
            "category_color": "secondary",  # 对应主页橙色
            "description": "从北京烤鸭到四川火锅，从上海小笼包到广东早茶，带您领略中国各地的美食文化。",
            "image_url": "https://picsum.photos/id/1040/800/600",
            "publish_date": "2023-06-20",
            "views": "3,127"
        },
        {
            "id": 3,
            "title": "体验中国传统文化活动",
            "category": "文化体验",
            "category_color": "green-500",  # 新增绿色类别
            "description": "参与中国传统手工艺制作、学习书法绘画、观看京剧表演，深入体验中国文化魅力。",
            "image_url": "https://picsum.photos/id/1041/800/600",
            "publish_date": "2023-07-10",
            "views": "1,892"
        }
    ]
    guide = next((g for g in guides if g['id'] == guide_id), None)
    if guide is None:
        return "攻略未找到", 404
    return render_template('guide_detail.html', guide=guide)


# 模拟更多景点数据（实际需从数据库查询）
attractions = [
    {
        "name": "北京",
        "category": "历史文化名城",
        "category_color": "primary",
        "description": "中国的首都，拥有众多历史古迹，如故宫、长城等。",
        "features": "故宫、长城、颐和园",
        "image_url": "https://picsum.photos/id/1001/800/600"
    },
    {
        "name": "西安",
        "category": "历史文化名城",
        "category_color": "primary",
        "description": "古代丝绸之路的起点，有兵马俑等著名古迹。",
        "features": "兵马俑、古城墙、大雁塔",
        "image_url": "https://picsum.photos/id/1002/800/600"
    },
    {
        "name": "成都",
        "category": "休闲旅游胜地",
        "category_color": "secondary",
        "description": "以美食和大熊猫闻名，充满悠闲的生活氛围。",
        "features": "大熊猫基地、武侯祠、锦里",
        "image_url": "https://picsum.photos/id/1003/800/600"
    }
]


# 新增更多景点路由
@app.route('/more_attractions')
def more_attractions():
    return render_template('more_attractions.html', attractions=attractions)

@app.route('/yuyue')
def yuyue():
    conn = connect_db()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM hotel_reservations")
    hotel_bookings = cursor.fetchall()
    cursor.execute("SELECT * FROM flight_reservations")
    flight_bookings = cursor.fetchall()
    cursor.execute("SELECT * FROM package_reservations")
    package_bookings = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('yuyue.html', hotel_bookings=hotel_bookings, flight_bookings=flight_bookings, package_bookings=package_bookings)


@app.route('/save_booking', methods=['POST'])
def save_booking():
    data = request.get_json()
    conn = connect_db()
    cursor = conn.cursor()
    if data['type'] == '酒店':
        # 查询当前最大编号
        cursor.execute("SELECT numbering FROM hotel_reservations ORDER BY numbering DESC LIMIT 1")
        max_numbering = cursor.fetchone()
        new_numbering = "000001"
        if max_numbering:
            new_numbering = str(int(max_numbering[0]) + 1).zfill(6)
        insert_query = """
        INSERT INTO hotel_reservations (hotel_name, check_in_date, check_out_date, room_type, appointment_category, numbering, operation)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (data['HotelName'], data['CheckInDate'], data['checkOutDate'], data['roomType'], "保证类预订", new_numbering, ""))
    elif data['type'] == '机票':
        cursor.execute("SELECT numbering FROM flight_reservations ORDER BY numbering DESC LIMIT 1")
        max_numbering = cursor.fetchone()
        new_numbering = "000001"
        if max_numbering:
            new_numbering = str(int(max_numbering[0]) + 1).zfill(6)
        insert_query = """
                INSERT INTO flight_reservations (place_of_departure, destinations, departure_date, flight_type, appointment_category, numbering, operation)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
        cursor.execute(insert_query, (data['departureAirport'], data['arrivalAirport'], data['departureDate'], data['Flight type'], "保证类预订", new_numbering, ""))
    elif data['type'] == '旅游套餐':
        cursor.execute("SELECT numbering FROM package_reservations ORDER BY numbering DESC LIMIT 1")
        max_numbering = cursor.fetchone()
        new_numbering = "000001"
        if max_numbering:
            new_numbering = str(int(max_numbering[0]) + 1).zfill(6)
        insert_query = """
        INSERT INTO package_reservations (destinations, travel_dates, number_of_people, package_type, appointment_category, numbering, operation)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (data['destination'], data['travelDate'], data['numPeople'], data['packageType'], "保证类预订", new_numbering, ""))
    conn.commit()
    cursor.close()
    conn.close()
    return 'Success'


@app.route('/get_bookings', methods=['GET'])
def get_bookings():
    conn = connect_db()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    # 查询酒店预订
    cursor.execute("""
        SELECT '酒店' AS type, 
               hotel_name, 
               check_in_date, 
               check_out_date, 
               room_type,
               appointment_category,
               numbering,
               operation
        FROM hotel_reservations
    """)
    hotel_bookings = cursor.fetchall()
    # 查询机票预订
    cursor.execute("""
        SELECT '机票' AS type, 
               place_of_departure, 
               departure_date, 
               destinations, 
               flight_type,
               appointment_category,
               numbering,
               operation
        FROM flight_reservations
    """)
    flight_bookings = cursor.fetchall()
    # 查询套餐预订
    cursor.execute("""
        SELECT '旅游套餐' AS type, 
               destinations, 
               travel_dates, 
               number_of_people, 
               package_type,
               appointment_category,
               numbering,
               operation
        FROM package_reservations
    """)
    package_bookings = cursor.fetchall()
    cursor.close()
    conn.close()
    all_bookings = hotel_bookings + flight_bookings + package_bookings
    return jsonify(all_bookings)


@app.route('/delete_booking', methods=['POST'])
def delete_booking():
    try:
        data = request.get_json()
        booking_id = data['id']
        conn = connect_db()
        cursor = conn.cursor()

        # 检查订单类型
        cursor.execute("""
            SELECT type FROM (
                SELECT '酒店' AS type, id FROM hotel_reservations WHERE id = %s
                UNION ALL
                SELECT '机票' AS type, id FROM flight_reservations WHERE id = %s
                UNION ALL
                SELECT '旅游套餐' AS type, id FROM package_reservations WHERE id = %s
            ) AS subquery
        """, (booking_id, booking_id, booking_id))

        booking_type = cursor.fetchone()
        if not booking_type:
            return '订单不存在', 404

        table_name = {
            '酒店': 'hotel_reservations',
            '机票': 'flight_reservations',
            '旅游套餐': 'package_reservations'
        }[booking_type[0]]

        # 执行删除
        cursor.execute(f"DELETE FROM {table_name} WHERE id = %s", (booking_id,))
        conn.commit()
        return 'Success'

    except Exception as e:
        conn.rollback()
        return f'数据库错误: {str(e)}', 500
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)