from openai import OpenAI
import os

# Ensure you have set your API key in your environment variables
# os.environ['OPENAI_API_KEY'] = 'your-api-key-here'

client = OpenAI()

def generate_story(prompt):
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a scary horror story teller, skilled in raising the hairs of your readers and eliciting goosebumps on their skin. You weave simple to understand yet complex stories with a chilling creative flair."},
                {"role": "user", "content": f"Tell a story about {prompt}"}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"An error occurred while generating the story: {e}")
        return None

def generate_image_prompts(story):
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an AI assistant skilled at creating descriptive image prompts based on story content."},
                {"role": "user", "content": f"Based on the following horror story, generate two brief but descriptive image prompts that capture key scenes or elements from the story. Each prompt should be no more than 15 words long.\n\nStory: {story}"}
            ]
        )
        prompts = completion.choices[0].message.content.split('\n')
        return [prompt.strip() for prompt in prompts if prompt.strip()]
    except Exception as e:
        print(f"An error occurred while generating image prompts: {e}")
        return None

def generate_images(prompts):
    images = []
    try:
        for prompt in prompts:
            response = client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1024",
                quality="standard",
                n=1,
            )
            images.append(response.data[0].url)
        return images
    except Exception as e:
        print(f"An error occurred while generating images: {e}")
        return None

def main():
    # Get user input for the story prompt / Hardcode the prompt for testing.
    story_prompt = "A possessive and monterous phone that steals life from its user."

    # Generate the story
    story = generate_story(story_prompt)
    if story:
        print("\nGenerated Story:")
        print(story)
        print("\n" + "="*50 + "\n")

        # Generate image prompts based on the story
        image_prompts = generate_image_prompts(story)
        if image_prompts:
            print("Generated Image Prompts:")
            for prompt in image_prompts:
                print(f"- {prompt}")
            print("\n" + "="*50 + "\n")

            # Generate images based on the prompts
            image_urls = generate_images(image_prompts)
            if image_urls:
                print("Generated Image URLs:")
                for url in image_urls:
                    print(url)
        else:
            print("Failed to generate image prompts.")
    else:
        print("Failed to generate the story.")

if __name__ == "__main__":
    main()