SELECT city.city_id, city.city, customer.first_name, customer.last_name, customer.email, address.address
FROM customer
LEFT JOIN address
ON customer.address_id = address.address_id
LEFT JOIN city
ON address.city_id = city.city_id
WHERE city.city_id = 312

SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name
FROM film
LEFT JOIN film_category
ON film_category.film_id = film.film_id
LEFT JOIN category
ON category.category_id = film_category.category_id
WHERE category.name = 'Comedy'

SELECT actor.actor_id, CONCAT(actor.first_name, ' ', actor.last_name) AS name, film.title, film.description, film.release_year
FROM actor
LEFT JOIN film_actor
ON  film_actor.actor_id = actor.actor_id
LEFT JOIN film
ON  film.film_id = film_actor.film_id
WHERE actor.actor_id = 5

SELECT store.store_id, city.city_id, customer.first_name, customer.last_name, customer.email, address.address
FROM store
LEFT JOIN customer
ON customer.store_id = store.store_id
LEFT JOIN address
ON customer.address_id = address.address_id
LEFT JOIN city
ON address.city_id = city.city_id
WHERE store.store_id = 1 AND city.city_id = 1 OR store.store_id = 1 AND city.city_id = 42 OR store.store_id = 1 AND city.city_id = 312 OR city.city_id = 459;

SELECT film.title, film.description, film.release_year, film.rating, film.special_features
FROM film
LEFT JOIN film_actor
ON film_actor.film_id = film.film_id
WHERE film_actor.actor_id = 15 AND film.rating = 'G' AND film.special_features LIKE '%Behind The Scenes%'

SELECT film.film_id, film.title, film_actor.actor_id, concat(actor.first_name, ' ', actor.last_name) AS name
FROM actor
LEFT JOIN film_actor
ON  film_actor.actor_id = actor.actor_id
LEFT JOIN film
ON  film.film_id = film_actor.film_id
WHERE film.film_id = 369

SELECT film.description, film.title, film.release_year, film.rating, film.special_features, category.name
FROM film
LEFT JOIN film_category
ON film_category.film_id = film.film_id
LEFT JOIN category
ON category.category_id = film_category.category_id
WHERE film.rental_rate = 2.99 AND category.name = 'Drama'

SELECT film.description, film.title, film.release_year, film.rating, film.special_features, category.name, concat(actor.first_name, ' ', actor.last_name) AS name
FROM category
LEFT JOIN film_category
ON film_category.category_id = category.category_id
LEFT JOIN film
ON film_category.film_id = film.film_id
LEFT JOIN film_actor
ON film.film_id = film_actor.film_id
LEFT JOIN actor
ON film_actor.actor_id = actor.actor_id
WHERE category.name = 'Action' AND actor.first_name = 'SANDRA' AND actor.last_name = 'KILMER'




