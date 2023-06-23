SELECT film.title, film.film_id , rental.return_date
FROM film
JOIN inventory ON inventory.film_id=film.film_id
JOIN rental ON rental.inventory_id=inventory.inventory_id
WHERE rental.return.return_date
BETWEEN rental.return_date '2005-05-29' AND '2005-05-31'