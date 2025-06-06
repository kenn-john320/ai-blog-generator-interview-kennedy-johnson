# SEO Research -> Search Engine Optimization Research


# Basic template for what I need
from flask import Flask
from seo_fetcher import random_metrics


app = Flask(__name__)

@app.route('/generate', methods=["GET"])
def generate(): 
    keyword = request.args.get("keyword")
    
    if not keyword:
        return jsonify({"error":"Keyword is required "}), 400

    seo_metrics = random_metrics(keyword)
    blog_post = generate_blog(keyword, seo_metrics)


    return jsonify({
        "keyword": keyword,
        "seo": seo_metrics,
        "content": blog_post
        })

if __name__ == '__main__':
    app.run(debug=True)