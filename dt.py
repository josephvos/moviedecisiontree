dt = {
    "question": "Do you want an animated or non-animated movie? (animated/non-animated) ",

    "branches": {

        "animated": {
            "question": "Should it be rated R? (yes/no) ",

            "branches": {

                "yes": "A (Animated) + R (Rated R) -> Akira (1988)",

                "no": {
                    "question": "Do you want animal main characters? (yes/no) ",

                    "branches": {

                        "yes": {
                            "question": "Do you want a western or non-western movie? (western/non-western) ",

                            "branches": {
                                "western": "(A (Animated) + ~R (Non-Rated R)) + ((N (Animal Main Characters) + W (Western)) -> Rango (2011)",

                                "non-western": {
                                    "question": "Do you want fighting or non-fighting movie? (fighting/non-fighting) ",

                                    "branches": {
                                        "fighting": "(A (Animated) + ~R (Non-Rated R)) + ((N (Animal Main Characters) + ~W (Non-Western)) + F (Fighting) -> Kung-Fu Panda (2008)",

                                        "non-fighting": "(A (Animated) + ~R (Non-Rated R)) + ((N (Animal Main Characters) + ~W (Non-Western)) + ~F (Non-Fighting) -> Over The Hedge (2006)",
                                    },
                                },
                            },
                        },

                        "no": {
                            "question": "Do you want a super hero movie? (yes/no) ",

                            "branches": {

                                "yes": {
                                    "question": "Do you want Marvel or non-Marvel? (marvel/non-marvel) ",

                                    "branches": {
                                        "marvel": "(A (Animated) + ~R (Non-Rated R)) + (~N (Animal Characters) + M (Marvel)) -> Across The SpiderVerse (2023)",

                                        "non-marvel": {
                                            "question": "Do you want DC or non-DC? (dc/non-dc) ",

                                            "branches": {

                                                "dc": "(A (Animated) + ~R (Non-Rated R)) + (~N (Animal Characters) + (~M (Not Marvel) + D (DC)) -> Lego Batman (2017)",

                                                "non-dc": "(A (Animated) + ~R (Non-Rated R)) + (~N (Animal Characters) + (~M (Not Marvel) + ~D (Not DC)) -> Big Hero 6 (2014)",
                                            },
                                        },
                                    },
                                },
                                "no": {
                                    "question": "Do you want a Lego movie? (yes/no) ",

                                    "branches": {

                                        "yes": "(A (Animated) + ~R (Non-Rated R)) + L (Lego Movie)) -> Lego Movie (2014)",

                                        "no": {
                                            "question": "Do you want a Spanish-themed movie? (yes/no) ",

                                            "branches": {
                                                "yes": "(A (Animated) + ~R (Non-Rated R)) + (~N (Animal Characters) + ~L (Not Lego) + S (Spanish Themed)) -> Coco (2017)",

                                                "no": "(A (Animated) + ~R (Non-Rated R)) + (~N (Animal Characters) + ~L (Not Lego) + ~S (Not Spanish Themed)) -> Despicable Me (2010)",
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },

        "non-animated": {
            "question": "Should it be rated R? (yes/no) ",

            "branches": {

                "no": {
                    "question": "Do you want a super hero movie? (yes/no) ",

                    "branches": {
                        "yes": "((~A (Animated) + ~R (Rated R)) + S (Superhero Film) -> Avenger Infinity War (2018))",

                        "no": {
                            "question": "Do you want a comedy? (yes/no) ",

                            "branches": {
                                "yes": "((~A (Animated) + ~R (Rated R)) + (~S (Not Superhero) + C (Comedy)) -> Taladega Nights (2006))",

                                "no": {
                                    "question": "Do you want a racing movie? (yes/no) ",

                                    "branches": {
                                        "yes": "((~A (Animated) + ~R (Rated R)) + ((~S (Not Superhero) + ~C (Not Comedy)) + R (Racing)) -> Gran Turismo (2023)",

                                        "no": {
                                            "question": "Should it be based off a book? (yes/no) ",

                                            "branches": {
                                                "yes": "((~A (Animated) + ~R (Rated R)) + (((~S (Not Superhero) + ~C (Not Comedy)) + ~R (Not Racing)) + B (Based on Book)) -> The Great Gatsby (2013)",

                                                "no": "((~A (Animated) + ~R (Rated R)) + (((~S (Not Superhero) + ~C (Not Comedy)) + ~R (Not Racing)) + ~B (Not Based on Book)) -> Now You See Me (2013)",
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    }
                },

                "yes": {
                    "question": "Do you want it to be primarily about historical figures? (yes/no) ",
                    "branches": {

                        "yes": {
                            "question": "Should it have a World War II premise? (yes/no) ",

                            "branches": {
                                "yes": {
                                    "question": "Do you want a biopic? (yes/no) ",

                                    "branches": {
                                        "yes": "((~A (Animated) + ~R (Rated R)) + ((~H (Not Historical) + B (Biopic)) + W (World War II)) -> Oppenheimer (2023)",

                                        "no": "((~A (Animated) + ~R (Rated R)) + ~H (Not Historical) + ~B (Not Biopic)) + W (World War II) -> 1917 (2019)",
                                    },
                                },
                                "no": "((~A (Animated) + ~R (Rated R)) + ~H (Not Historical) + ~B (Not Biopic) + ~W (World War II)) -> Gladiator (2000)",
                            },
                        },


                        "no": {
                            "question": "Do you want a comedy? (yes/no) ",

                            "branches": {
                                "yes": "((~A (Animated) + ~R (Rated R)) + (~H (Not Historical) + C (Comedy)) -> 21 Jump Street (2012)",

                                "no": "((~A (Animated) + ~R (Rated R)) + (~H (Not Historical) + ~C (Not Comedy)) -> Whiplash (2014)",
                            },
                        },
                    },
                },
            },
        },
    },
}
