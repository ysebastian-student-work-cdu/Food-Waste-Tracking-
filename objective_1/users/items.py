from . import views

class Item_Class:
    
    items= []
         
    def find(name):
        for item in Item_Class.items:
            if item.name == name:
                return item
            
        return Item_Class.names[item]

    def getItems():
        return Item_Class.items
     

    
    def __init__(self, name, title = '', content = '', images = ''):
        self.name = name
        self.title = title
        self.content = content
        self.images = images
        self.addItem()
        
    
    # Adds a new page entry to the static dictionary 
    def addItem(self):
        Item_Class.items.append(self)

        
        
        
item_list = []
	

reasons = Item_Class(

    name = 'reasons',

    title = 'Why food waste is a problem', 

    content = ['''
        <h2>
            Climate impact to a warming planet
        </h2>
        <p>
            What do flying, plastic production and oil extraction have in common? All these activities have a lower emissions impact on our warming planet than food waste.
            At an estimated 8% contributer of worldwide carbon emissions according to United Nations FAO, the everyday throwing away of that soggy lettuce you took too long to eat culminates into
            a much bigger impact on the planet than we thought.
        </p>
        <p>
            As it turns out, through minimal decision making each week, you can play your part in a significant role of helping to reduce worldwide carbon emissions by 8%. Sounds like a good deal to me!
        </p>''',
        '''
        <h2>
            Economic Impact
        </h2>
        <p>
            Food waste is quite costly, impacting the world economy $940 billion per year and the Australians economy around $36.6 billion each year according to the DCCEEW Government Department. But how does this affect the cost of
            your daily bread you ask? Consumers create the bulk of the cost too in through the third of a bag of groceries the avergae Australian wastes each week which has been estimated to cost you around $1438.55 (780 pounds) per year.
            Now that's expensive!
        </p>
        '''
        ],

    images = ['users/images/melting_globe.png', 'users/images/money_bin.jpg'])




facts = Item_Class(
    
    name = 'impacts',

    title = "Facts about Food Waste",

    content = ['''
        <ul>

        <li>Approximately one-third of all food produced globally is lost or wasted. This amounts to 1.3 billion tons of food annually. (FAO)</li>

        <li>In high-income countries, per capita food waste by consumers is between 95-115 kg per year, while in sub-Saharan Africa and South/Southeast Asia, it is only 6-11 kg per year. (FAO)</li>

        <li>Food waste occurs at different stages of the food supply chain. In high-income countries, 40% of food waste occurs at the consumer level, while in low-income countries, 40% of food waste occurs at the post-harvest and processing stages. (FAO)</li>

        <li>Food waste contributes to greenhouse gas emissions and climate change. If food waste were a country, it would be the third-largest emitter of greenhouse gases after China and the United States. (FAO)</li>

        <li>The economic costs of food waste are significant. In the United States, the economic cost of food waste is estimated at $218 billion annually. (ReFED)</li>

        <li>Food waste exacerbates food insecurity and hunger. The amount of food wasted globally could feed 2 billion people, which is more than the number of undernourished people in the world. (FAO)</li>

        <li>Reducing food waste has significant environmental and economic benefits. For example, reducing food waste by 25% globally could feed 870 million people and save 8% of global freshwater resources. (FAO)</li>

        <li>Consumers can play an important role in reducing food waste. In the United States, households are responsible for 43% of all food waste, and reducing household food waste could save consumers up to $1,500 annually. (ReFED)</li>

        <li>Sustainable food production and consumption practices can help reduce food waste. For example, using sustainable agricultural practices, such as reducing pesticide use and improving soil health, can reduce food waste by increasing crop yields and reducing post-harvest losses. (FAO)</li>
        
        <li>Food recovery programs can help divert edible food from landfills and provide it to people in need. In the United States, food recovery programs could provide an additional 1.8 billion meals annually to people in need. (ReFED)</li>
    </ul>
    ''']    
)

resources = Item_Class(

    name = 'resources',
    
    title = "External Resources",

    content = ['''
    <ul>
        <li><a target="_blank" href='https://www.fao.org/home/en'>Food and Agriculture Organisation of the United Nations</a></li>

        <li><a target="_blank" href='https://refed.org/'>ReFED.org</a></li>

        <li><a target="_blank" href='https://www.ozharvest.org/food-waste-facts/'> OzHarvest</a></li>
        
        <li><a target="_blank" href='https://www.lovefoodhatewaste.nsw.gov.au/about-food-waste'>NSW Government: Love Food, Hate Waste</a></li>
        
        <li><a target="_blank" href='https://www.dcceew.gov.au/environment/protection/waste/food-waste'>Department of Climate Change, Energy, the Environment and Water</a></li>
        
        <li><a target="_blank" href='https://www.foodbank.org.au/food-waste-facts-in-australia/?'>FoodBank.org</a></li>
        
        <li><a target="_blank" href='https://www.hsph.harvard.edu/nutritionsource/sustainability/food-waste/'>Harvard School of Public Health</a></li>
        
        <li><a target="_blank" href='https://www.cleanup.org.au/foodwaste'>Cleanup.org</a></li>
        
        <li><a target="_blank" href='https://www.stopfoodwaste.com.au/'>Stop Food Waste</a></li>
        
        <li><a target="_blank" href='https://en.wikipedia.org/wiki/Food_loss_and_waste'>Wikipedia</a></li>
    </ul>
    ''']
)

solutions = Item_Class(

    name = 'solutions',

    title = "Solutions to Food Waste",

    content = ['''
        <ul>
        <li>Reducing overproduction: One solution to food waste is to reduce overproduction at every stage of the food supply chain, including at the farm level, processing and distribution centers, and retailers.</li>

        <li>Improving storage and transportation: Proper storage and transportation techniques can help to reduce spoilage and food waste. This includes using appropriate temperature control measures, packaging, and handling procedures.</li>

        <li>Food recovery and donation: Food recovery programs can help to divert edible food from landfills and provide it to people in need. These programs can involve donations to food banks, soup kitchens, and other community organizations.</li>

        <li>Educating consumers: Consumer education campaigns can help raise awareness about the impact of food waste and provide tips on how to reduce it at home. This includes education on proper food storage, meal planning, and portion control.</li>

        <li>Sustainable food production and consumption: Sustainable agriculture practices, such as reducing pesticide use and improving soil health, can help to reduce food waste by increasing crop yields and reducing post-harvest losses. Sustainable consumption practices, such as reducing food waste at home and choosing to buy only what is needed, can also help to reduce food waste.</li>

        <li>Standardizing expiration dates: Confusing expiration dates and labeling can cause consumers to waste edible food. Standardizing expiration dates and labeling can help consumers better understand when food is still safe to consume.</li>

        <li>Repurposing food waste: Repurposing food waste into animal feed, composting, or energy generation can help to reduce the amount of food waste that ends up in landfills.</li>

        <li>Encouraging innovation: Encouraging innovation in food waste reduction technologies, such as new packaging materials and improved processing techniques, can help to further reduce food waste.</li>
    </ul>        
            ''']

)

benefits = Item_Class(

    name = 'benefits',

    title = 'Benefits of Food Waste Reduction',

    content = ['''
    
    <ul>
        <li>Environmental benefits: Food waste reduction can help reduce greenhouse gas emissions and mitigate climate change. It can also help conserve natural resources such as water and energy.</li>

        <li>Economic benefits: Food waste reduction can lead to significant cost savings for businesses and households. This includes reducing the costs of purchasing, storing, and disposing of food waste.</li>
        
        <li>Social benefits: Food waste reduction can help reduce food insecurity and hunger by redirecting edible food to people in need. It can also help reduce the environmental and social impacts of food waste, such as soil and water pollution.</li>
        
        <li>Improved food security: By reducing food waste, more food is available for consumption, potentially improving food security for vulnerable populations.</li>
        
        <li>Improved public health: Reducing food waste can lead to improved public health outcomes, such as reducing the amount of food waste in landfills and reducing the production of methane gas.</li>
        
        <li>Increased efficiency in food systems: Reducing food waste can lead to increased efficiency in food systems, including reducing the amount of land, water, and other resources required for food production.</li>
        
        <li>Reputation and customer loyalty: Businesses that prioritize food waste reduction can improve their reputation and customer loyalty by demonstrating their commitment to environmental sustainability and social responsibility.</li>
        
        <li>Innovation and new business opportunities: Food waste reduction can spur innovation and the development of new technologies and business models, creating new economic opportunities and jobs in the food sector.</li>
    </ul>
    ''']

    
)

