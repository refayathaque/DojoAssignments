####

# INTRODUCTION

# creating, manipulating, and saving data.

# database, which is in charge of your data! Databases are merely collections of
# organized information that can easily be accessed, managed, and updated.

# ERD is short for 'Entity Relationship Diagram'. That's just a fancy way of saying
# that ERDs are essentially visual blueprints for how your database looks and behaves.

# When we normalize our tables, we DON'T REPEAT DATA. This means that in the long run,
# we can use our storage space more efficiently.

# IDs and the FOREIGN KEYs serve as the glue between our tables.

# we are using the strategy of NORMALIZING our tables and setting RELATIONSHIPS BETWEEN THEM
# because we want to SAVE STORAGE SPACE; and also because it makes our database more MODULAR
# so that we can create more variety of customized tables using SQL.

####

# ONE TO ONE

# Each TABLE should have its own UNIQUE IDENTIFIER, and should INCREMENT : ID

# FOREIGN KEYs can be put in a TABLE to reference things in ANOTHER TABLE.

# TABLE can be joined as long as there is a FOREIGN KEY that references ANOTHER TABLE'S ID.

# Since each address that we have can only belong to a single customer and each
# customer can only have one address, we call this a ONE TO ONE relationship.

# Examples of ONE TO ONE:
    # Customers and Credit Cards - Every Customer has one Credit Card, every Credit Card belongs to one Customer.
    # User and Email - Every User has one Email Address, every Email Address has one User.
    # Product and Image - Every Product has an Image, every Image is of a Product.

####

# ONE TO MANY

# e.g. Customers can place MULTIPLE orders... Since one customer can have many orders
# for any given user we call this a ONE TO MANY relationship.

# Using SQL to join different tables on the foreign key and the primary id.

# Examples of ONE TO MANY:
    # Messages and Comments - One Comment belongs to one Message, but one Message can have many Comments.
    # States and Cities - One City is only in one State, but one State can have many Cities.
    # Customers and Orders - One Order only has one Customer, but one Customer can have many Orders.

####

# MANY TO MANY

# e.g. Orders can have MANY items, items can have MANY orders...

# In a MANY TO MANY relationship, we create a CONNECTOR that has BOTH the order_id and the item_id
# so that we can determine all the items in a particular order.

# Anytime you have a MANY TO MANY, it will require some sort of CONNECTOR TABLE!

# Examples of MANY TO MANY:
    # Users and Interests - One User can have MANY Interests, one Interest can be applied to MANY Users.
    # Actresses and Movies - One Movie can have MANY Actresses, one Actress can be in MANY Movies.
    # Businesses and Cities - One Business can be spread across MANY Cities, one City can be home to MANY Businesses.

####

# NORMALIZATION

# NORMALIZATION is simply a convention for SPLITTING large tables of data into SMALLER SEPARATE tables with the primary
# goal being to NOT REPEAT DATA.

# If we want to store a user's email address, we'd want to store it in only one place. Then, if we ever need to refer to
# it again, we'd simply use the ID. The ID WILL NEVER CHANGE, so even if we update the user's email address, NONE OF THE
# OTHER CONNECTIONS we defined in our database will be damaged.

# First Form

# Each Column in your table can only have 1 value.
# Ex. You should not have an address column in your table that lists the address, city, state, and zip, all separated by commas.

# Second Form

# Each Column in your table that is not a key (primary or foreign) must have unique values.
# Ex. If you have a movies table with a categories column, you should not have a category repeated more than once.

# Third Form

# You cannot have a non-key column that is dependent on another non-key column.
# Ex. If you have a books table with columns publisher_name and publisher_address, the publisher_address and publisher_name
# should be separated into a separate table and linked to books with a foreign key. The publisher_address is dependent on
# the publisher_name and neither column is a key column.
