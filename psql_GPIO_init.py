import psycopg

useablePins = {3,4,17,27,22,5,6,13,26,23,24,25,12,16}

with psycopg.connect(
   dbname="test_gpio",
   user="testuser",
   password="password",
   host="127.0.0.1",
   port= '5432'
   ) as conn:
    
    with conn.cursor() as cur:

        cur.execute("TRUNCATE pin_info")
    
        for pin in useablePins:
            cur.execute("INSERT INTO pin_info (pin, I_O, HIGH_LOW) VALUES (%s, %s, %s)", 
            (pin, False, False))
            print(f"Data for {pin} Inserted")

        cur.execute("SELECT * FROM pin_info")
        result = cur.fetchall()
        print(f'Table looks like: {result}')

        conn.commit()