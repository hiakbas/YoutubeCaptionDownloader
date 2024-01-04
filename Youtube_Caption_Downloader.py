from youtube_transcript_api import YouTubeTranscriptApi

while True:
    # Get the YouTube video link from the user
    video_link = input("Please paste your youtube link:  ")

    # Check if the provided link is a valid YouTube link
    if "watch?v=" in video_link and "youtube.com" in video_link:
        # Extract the video ID from the link
        short_link = video_link.split("=")[1]

        # Get the list of available transcripts for the video
        transcript_list = YouTubeTranscriptApi.list_transcripts(short_link)

        # Print available transcripts
        for transcript in transcript_list:
            print(transcript)
    else:
        print("It is not a valid youtube link, Please try another one")
        continue

    while True:
        # Get the desired language for the transcript
        language = input("Please select language: ")

        try:
            # Get the transcript for the specified language
            srt = YouTubeTranscriptApi.get_transcript(short_link, languages=[language])
            break
        except:
            print("Please write a suitable language")
            continue

    # Write the subtitles to a text file
    with open("subtitles.txt", "w", encoding='utf8') as f:
        for i in srt:
            f.write("{}\n".format(i))

    last = ""
    with open('subtitles.txt', 'r', encoding="utf-8") as file:
        # Process the subtitles content to extract the text
        subtitles_content = file.read().split("{'text':")
        for i in subtitles_content:
            new = i.split(",")
            last = last + new[0].strip("' '") + " "

    # Write the processed subtitles to another text file
    with open("Last_version.txt", "w", encoding="utf-8") as f:
        f.write(last)

    print("It is done, Please check Last_version.txt")
    break
