import pymongo
from bson import ObjectId

# Need to debug the update issue using the id
client= pymongo.MongoClient("mongodb+srv://yt_manager:Yash1212@cluster1.rg9fwmm.mongodb.net/")

# Give name to dataBSE
db= client["ytmanager"]
# create collection 
video_collection= db["videos"]
print(video_collection)

def list_all_videos():
    for video in video_collection.find():
        # in mongo id are accessed using _id
        print(f"ID:{video['_id']},Name: {video['name']} and Time: {video['time']}")
def add_video(name, time):
    video_collection.insert_one({"name":name, "time":time})

    
def update_video(video_id, new_name, new_time):
    video_collection.update_one(
        {'_id':ObjectId(video_id)}, {"$set": {"name":new_name, "time":new_time}}
    )
def delete_video(video_id):
    video_collection.delete_one({"_id":ObjectId(video_id)})

def main():
    while True:
        print("Youtube manager app")
        print("1. List all videos")
        print("2. Add a new video")
        print("3. Update the video")
        print("4. Delete a video")
        print("5. Exit the app")
        choice= input("Enter your choice")

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
                delete_video(video_id)
                
            case '5':
                break
            case _:
                print("Invalid Choice")


if __name__=="__main__":
    main()