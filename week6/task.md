1. in the context of the online shop, Write a REST API specification concerning the items ignore the status codes

  GET /store // gets all items currently in store

  GET /store/items/{itemId} // returns the item object form backend
  PUT /store/items/{itemId} //modifies the item object with requestbody data

  GET /store/orders //gets alll orders
  GET /store/orders/{orderId} //gets a specific order

2. consider a Class Customer , give an example of a bad and a good interface in the context of the online shop (backend)

  good: Customer.getId(), Customer.getCart() , Customer.getPaymentInfo(CustomerEmail), Customer.createOrder(Order), Customer.delete(),Customer.block()

3. Now your tasked with creating an api for payment via online shops, complete ignoring the constraints and implementation details, how would an ideal interface look like?
  api.setClient(paymentinfo,clientId)
  api.createInvoice(invoice,clinetId)
  api.getInvoices()
  api.getClientInvoice(clientId)
  api.getPaymentHistory(clientId)
  api.setTwintPayment(invoice,clientId)

4. Why might it not be possible to follow such an ideal api ?
  security reasons, passing data that way even via https might be too dangerous considering the data is extremely sensistive, also
  how does the api know that the client actually did consent to the invoice? an api like that could be very easily exploited
