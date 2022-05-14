# Building an Online Shop
#### Video Demo:  <URL HERE>
#### Description:
1. ### General Context

    Ecommerce is the process of buying and selling tangible products and services online. It involves more than one party along with the exchange of data or currency to process a transaction. 
    It is part of the greater industry that is known as electronic business (ebusiness), which involves all of the processes required to run a company online.

    Ecommerce has helped businesses (especially those with a narrow reach like small businesses) gain access to and establish a wider market presence by providing cheaper and more efficient distribution channels for their products or services. 
    Target (TGT) supplemented its brick-and-mortar presence with an online store that allows customers to purchase everything from clothes and coffeemakers to toothpaste and action figures right from their homes.

    Ecommerce operates in all four of the following major market segments. These are:

    - Business to business (B2B), which is the direct sale of goods and services between businesses
    - Business to consumer (B2C), which involves sales between businesses and their customers
    - Consumer to consumer, which allows individuals to sell to one another, usually through a third-party site like eBay
    - Consumer to business, which lets individuals sell to businesses, such as an artist selling or licensing their artwork for use by a corporation

    Providing goods and services isn't as easy as it may seem. It requires a lot of research about the products and services you wish to sell, the market, audience, competition, as well as expected business costs.

    Once that's determined, you need to come up with a name and set up a legal structure, such as a corporation. 
    Next, set up an ecommerce site with a payment gateway. 
    For instance, a small business owner who runs a dress shop can set up a website promoting their clothing and other related products online and allow customers to make payments with a credit card or through a payment processing service, such as PayPal

2. ### Conception

    - #### Database Model Schema
         ![Database Schema](/myshop/assets/shema%20data%20base.png)
        - #### Explanation of each entity :
            These are the Categorie, Product, Customer, Cart and Order models. 

            - The Category model consists of :
                - categorie_name field and a unique id field (unique implies the creation of an index). 
            - The Product entity fields are as follows:
                - id: A unique id field (unique implies the creation of an index). 
                - categorie_id: A ForeignKey to the Category entity. This is a one-to-many
                - relationship: a product belongs to one category and a category contains
                multiple products.
                - product_name: The name of the product.
                - product_price: This field uses Python's Float type to store a fixedprecision decimal number.
                - image_path: An optional product image.
                - product_description: An optional description of the product.
                - product_size: An optional size of the product.
                - available: A Boolean value that indicates whether the product is available
                or not. It will be used to enable/disable the product in the catalog.
            - The Customer entity fields are as follows:
                - id: A unique id field (unique implies the creation of an index). 
                - username: The name of the customer.
                - email: The emial of the customer.
                - address: The address of the customer.
                - password: The password of the customer.
                - is_admin: A Boolean value that indicates whether the user is admin
                - relationship: a cutomer have one cart and a multiple orders
            - The Cart and Order models fields are as the follows:
                - id: A unique id field (unique implies the creation of an index). 
                - customer_id: A ForeignKey to the Customer entity.
    - #### Application Features:
        - Users will be able to browse through a product catalog.

        ![catalogue](/myshop/assets/catalogue.png)
        - Also, user can add products to a shopping cart after creating an account and be loged in.
        ![alt](/myshop/assets/cart.png)

        ![alt](/myshop/assets/login.png)

        - Finally, they will be able to check out the cart and place an order.
        ![alt](/myshop/assets/order.png)

        - The administrator can add products and manage every data in the application after be loged in.
        ![alt](/myshop/assets/admin_home.png) 

        ![alt](/myshop/assets/admin_add_product.png)       
3. ### Implementation

    - #### The Technologies Used:
        - #### BackEnd 
            - Flask: is a small and lightweight Python web framework that provides useful tools and features that make creating web applications in Python easier. It gives developers flexibility and is a more accessible framework for new developers since you can build a web application quickly using only a single Python file.
            - Jinja: also commonly referred to as "Jinja2" to specify the newest release version, is a Python template engine used to create HTML, XML or other markup formats that are returned to the user via an HTTP response.
            - PostgreSQL: is used as the primary data store or data warehouse for many web, mobile, geospatial, and analytics applications. The latest major version is PostgreSQL
            - Visual Studio Code: is a streamlined code editor with support for development operations like debugging, task running, and version control.
        - #### FrontEnd
            - HTML and CSS: CSS is the acronym of “Cascading Style Sheets”. CSS is a computer language for laying out and structuring web pages (HTML).
            - Bootstrap: is a potent front-end framework used to create modern websites and web apps. Bootstrap also supports JavaScript extensions. 
        - #### Infrastructure
            - AWS API Gateway Lambda Zappa: used to build and deploy.
            - Amazon Simple Email Service (SES): is a cost-effective, flexible, and scalable email service that enables developers to send mail from within any application