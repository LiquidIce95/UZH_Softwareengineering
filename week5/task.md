1. In the context of the online shop from the previous exercise, decompose the following user story step by step and comment on how each step 
reveals certain asepcts about your architecture

  As a user I want to create an account to store items I might buy later.

step1. identify nouns: user, account, store , items and implicitly cart
we could model these actors and entities as classes 
  User: email,password,id,cart,payment info,credit credibility,Statistics
  Cart: items,gettotalcost,createInvoice
  item: cost,stockStatus,Statistics,description,id

  this also already gives us a class diagram with some relations

step2: identify verbs( actions):creating, store,buy

  storing implies data persistence of user data inlcuding the cart and items
  account creation implies a interface at the front end for the user to enter data
  buy implies either creating or using existing apis for online shop payment

step3: identify relations among entities
  already perceived: carts consist of items, a User has one cart (or could have multiple carts for comparison?)
  definite payment must only occure with users absolute consent and must be secure
  item description (and other data) must it make possible to be searchable for the user

  also the cart can only contain items which are shipable

2. Draw a sequence diagram for this user story, what additional realtionships did you find?

  user should be verified before being able to make orders especially on invoice, since this could be malicously exploited
  in addition to a cart, a wishlist could be helpful for customers saving items that are not available but want to buy in the future

