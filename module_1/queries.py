SELECT_ALL = 'SELECT character_id, name FROM charactercreator_character;'

SELECT_AVG_ITEM_WEIGHT = '''
SELECT cc_char.name, AVG(ai.weight) AS avg_item_weight from charactercreator_character AS cc_char
JOIN charactercreator_character_inventory AS cci
ON cc_char.character_id = cci.character_id
JOIN armory_item as ai
on cci.item_id = ai.item_id
GROUP BY cc_char.character_id;
'''