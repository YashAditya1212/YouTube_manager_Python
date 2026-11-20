import sqlite3
# //Connection string
conn= sqlite3.connect('youtube_videos.db')
# it wil return an object which will help us to run the queries
cursor= conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
        )
''')


def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)
def add_video(name, time):
    cursor.execute("INSERT INTO videos(name, time) VALUES (?, ?)", (name,time))

    # commit
    conn.commit()
def update_video(video_id,new_name, new_time):
    cursor.execute("UPDATE videos SET name= ?, time = ? WHERE id= ?", (new_name, new_time, video_id))
    conn.commit()
def delete_video(video_id):
    cursor.execute("DELETE FROM videos where id= ?", (video_id,))
    # tuple(single_el, )
    conn.commit()
    
def main():
    while True:
        print("Youtube manager app with DB")
        print("\n")
        print("1. List videso")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exit app")
        choice = input("Enter your choice: ")

        # switch is match in python
        match choice:
            case '1':
                list_all_videos()
            case '2':
                name= input("Enter the video name: ")
                time= input("Enter the video time: ")
                add_video(name,time)
            case '3':
                video_id=input("Enter the video id")
                new_name= input("Enter the video name: ")
                new_time= input("Enter the video time: ")
                update_video(video_id,name,time)
            case '4':
                video_id=input("Enter the video id to delete")
                name= input("Enter the video name: ")
                time= input("Enter the video time: ")
                delete_video(video_id,name,time)
                
            case '5':
                break
            case _:
                print("Invalid Choice")

    conn.close()

if __name__ == "__main__":
    main()