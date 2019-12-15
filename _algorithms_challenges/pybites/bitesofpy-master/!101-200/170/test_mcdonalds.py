from Previous.mcdonalds import (df,
                                get_food_most_calories,
                                get_bodybuilder_friendly_foods)

ASSERT_ERROR = ("One or more expected foods not in "
                "get_bodybuilder_friendly_foods's return value")


def test_get_food_most_calories():
    actual = get_food_most_calories()
    expected = 'Chicken McNuggets (40 piece)'
    assert actual == expected


def test_get_food_most_calories_smaller_population():
    """Extra test to prevent hardcoding the return value"""
    df_breakfast = df[df['Category'] == 'Breakfast']

    actual = get_food_most_calories(df_breakfast)
    expected = 'Big Breakfast with Hotcakes (Large Biscuit)'
    assert actual == expected


def test_get_bodybuilder_friendly_foods():
    actual_with_drinks = list(get_bodybuilder_friendly_foods())
    expected = ['Premium Bacon Ranch Salad with Grilled Chicken',
                'Nonfat Latte (Small)',
                'Nonfat Latte (Large)',
                'Premium Southwest Salad with Grilled Chicken',
                'Nonfat Latte (Medium)']
    assert all(food in actual_with_drinks for food in expected), ASSERT_ERROR


def test_get_bodybuilder_friendly_foods_excluding_liquid_food():
    actual_wo_drinks = list(get_bodybuilder_friendly_foods(excl_drinks=True))
    expected = ['Premium Bacon Ranch Salad with Grilled Chicken',
                'Premium Southwest Salad with Grilled Chicken',
                'Premium Grilled Chicken Classic Sandwich',
                'Premium Grilled Chicken Ranch BLT Sandwich',
                'Premium Grilled Chicken Club Sandwich']
    assert all(food in actual_wo_drinks for food in expected), ASSERT_ERROR