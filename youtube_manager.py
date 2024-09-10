import json

# Load data from file
def load_data():
    try:
        with open('youtube.txt', 'r') as file:  # Fixed the 'open' syntax
            return json.load(file)
    except FileNotFoundError:
        return []  # Return an empty list if the file is not found
    except json.JSONDecodeError:
        return []  # Handle the case where the file is empty or corrupted

# Save data to file
def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:  # Fixed the file mode 'w'
        json.dump(videos, file, indent=4)  # Added indent for pretty-printing

# List all videos with index
def list_all_videos(videos):
    if not videos:
        print("No videos available.")
    else:
        for index, video in enumerate(videos, start=1):
            print(f"{index}. {video['name']} (Duration: {video['time']})")

# Add a new video
def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video duration: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)
    print(f"Video '{name}' added successfully!")

# Update an existing video
def update_video(videos):
    list_all_videos(videos)
    video_index = int(input("Enter the number of the video to update: ")) - 1
    if 0 <= video_index < len(videos):
        name = input("Enter new video name (leave blank to keep the same): ")
        time = input("Enter new video duration (leave blank to keep the same): ")

        if name:
            videos[video_index]['name'] = name
        if time:
            videos[video_index]['time'] = time

        save_data_helper(videos)
        print("Video updated successfully!")
    else:
        print("Invalid video number!")

# Delete a video
def delete_video(videos):
    list_all_videos(videos)
    video_index = int(input("Enter the number of the video to delete: ")) - 1
    if 0 <= video_index < len(videos):
        deleted_video = videos.pop(video_index)
        save_data_helper(videos)
        print(f"Video '{deleted_video['name']}' deleted successfully!")
    else:
        print("Invalid video number!")

# Main loop
def main():
    videos = load_data()

    while True:
        print("\nYouTube Manager | Choose an option")
        print("1. List all YouTube videos")
        print("2. Add a YouTube video")
        print("3. Update YouTube video details")
        print("4. Delete a YouTube video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

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
                print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()