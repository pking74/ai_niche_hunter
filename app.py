from flask import Flask, render_template, request, redirect, url_for
import openai

app = Flask(__name__)

# Replace with your actual OpenAI API key
openai.api_key = 'your-openai-api-key-here'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_subniches', methods=['POST'])
def generate_subniches():
    main_niche = request.form['niche']
    
    # OpenAI API call to generate sub-niches and content ideas
    prompt = f"Generate 5 sub-niches and 5 content topic ideas within each sub-niche for the niche: {main_niche}"
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.7,
    )
    
    subniches_ideas = response.choices[0].text.strip()

    return render_template('subniches.html', niche=main_niche, ideas=subniches_ideas)

@app.route('/generate_keywords', methods=['POST'])
def generate_keywords():
    selected_subniche = request.form['subniche']
    
    # OpenAI API call to generate keyword-optimized article ideas
    prompt = f"Generate 20 keyword-optimized article ideas for the sub-niche: {selected_subniche}"
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.7,
    )
    
    keyword_ideas = response.choices[0].text.strip()

    return render_template('keywords.html', subniche=selected_subniche, keywords=keyword_ideas)

if __name__ == '__main__':
    app.run(debug=True)
