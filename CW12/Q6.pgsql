SELECT first_name, last_name, fil.title, (rental.return_date - rental.rental_date)
FROM customer
JOIN rental ON customer.customer_id = rental.customer_id
JOIN film ON inventory.film_id = film.film_id;

