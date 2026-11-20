import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
            
def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
       
        # start 0 se na hi 1 se ho
        # without enumerate bhi kaam chal jaega but aage update aur delete karna hai without indexing konsi karna hai nhi pata chalega na 
        print(f"{index}. {video['name']}, Duration: {video['time']}")
        # dictionary access using {name['name']}
    print("\n")
    print("*" * 70)

def add_video(videos):
    name= input("Enter video name")
    time= input("Enter video time")
    videos.append({'name':name, 'time':time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index=int(input("Eneter the video number to update"))

    if 1<= index <= len(videos):
        name=input("Enter the new video name")
        time= input("ENter the video time")
        videos[index-1] = {'name':name, 'time': time}
        save_data_helper(videos)

    else:
        print("Invalid number")


def delete_video(videos):
    list_all_videos(videos)
    index=int(input("Eneter video number to delete"))

    if 1<= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)

    else:
        print("Invalid input")


def main():

    videos=load_data()
    # it will keep on checking the user input
    while True:
        print("\n Youtube Manager | choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice= input("Enter your Choice ")

        print(videos)

        # switch is match in python
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice")



# Running main this is the follwoed practice. IF main found execute it 
if __name__ ==  "__main__":
    main() 