import random

def random_metrics(keyword):
    
    # More context for project and expectations
    
    
    # SEO Research -> Search Engine Optimization Research
 
    # search_volume: How many times a word is searched on Google/Bing/etc (use int)
    
    # keyword_difficulty: SEO in a score, scaled from 1-100. Higher the score, higher more competitive the keyword. (int 1-100)
    
    # avg_cpc: Average cost per click! The average cost per click (is calculated by dividing the total cost of clicks by the total number of clicks. (float since it could be a decimal)
    
    # Return a dictionary of random values
    return {
        'search_volume': random.randint(1000,100000),
        'keyword_difficulty': random.randint(1,100),
        'averageClicksperCost': round(random.uniform(1.25, 99.99), 2)
    }