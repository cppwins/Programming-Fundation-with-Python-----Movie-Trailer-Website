# entertainment_center.py

import media, fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that comes to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

grand_budapest = media.Movie("The Grand Budapest Hotel",
                             "Mr.Gustave and Zero's bizzar advanture and the rise and fall of European most famous hotel",
                             "http://upload.wikimedia.org/wikipedia/zh/a/a6/The_Grand_Budapest_Hotel_Poster.jpg",
                             "https://www.youtube.com/watch?v=1Fg5iWmQjwk")

interstellar = media.Movie("Interstellar",
                           "A group of astronauts travel through a worm hole to find habitable planet to save mankind",
                           "http://www.hollywoodreporter.com/sites/default/files/custom/Blog_Images/interstellar2.jpg",
                           "https://www.youtube.com/watch?v=0vxOhd4qlnA")

life_of_pi = media.Movie("Life of Pi",
                         "An indian boy survives 227 days after a shipwreck while stranded on a lifeboat in the Pacific Ocean with a Bengal tiger named Richard Parker.",
                         "http://upload.wikimedia.org/wikipedia/en/5/57/Life_of_Pi_2012_Poster.jpg",
                         "www.youtube.com/watch?v=j9Hjrs6WQ8M")

a_good_year = media.Movie("A Good Year",
                          "Yound bond trader Max Skinner goes back to his late Uncle Henry's vineyard estate in Provence, Fance, and all the distant memory comes back to him.",
                          "http://upload.wikimedia.org/wikipedia/en/4/47/A_Good_Year.jpg",
                          "www.youtube.com/watch?v=-zmhOP4uArQ")
            

movies = [toy_story, avatar, grand_budapest, interstellar, life_of_pi, a_good_year]
fresh_tomatoes.open_movies_page(movies)
