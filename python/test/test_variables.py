from src.Items.NormalItem import *
from src.Items.AgedBrie import *
from src.Items.Backstage import *
from src.Items.Conjured import *
from src.Items.Sulfuras import *
'''
At this file I will store all the variables needed to check if the software
complete each routines correctly, creating an array of objects.
'''


items_day_zero = [NormalItem("+5 Dexterity Vest", 10, 20),
                AgedBrie("Aged Brie", 2, 0),
                NormalItem("Elixir of the Mongoose", 5, 7),
                Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80),
                Sulfuras("Sulfuras, Hand of Ragnaros", -1, 80),
                Backstage("Backstage passes to a TAFKAL80ETC concert", 15, 20),
                Backstage("Backstage passes to a TAFKAL80ETC concert", 10, 49),
                Backstage("Backstage passes to a TAFKAL80ETC concert", 5, 49),
                Conjured("Conjured Mana Cake", 3, 6)
                ]

items_day_one = [NormalItem("+5 Dexterity Vest", 9, 18),
                AgedBrie("Aged Brie", 1, 1),
                NormalItem("Elixir of the Mongoose", 4, 6),
                Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80),
                Sulfuras("Sulfuras, Hand of Ragnaros", -1, 80),
                Backstage("Backstage passes to a TAFKAL80ETC concert", 14, 21),
                Backstage("Backstage passes to a TAFKAL80ETC concert", 9, 50),
                Backstage("Backstage passes to a TAFKAL80ETC concert", 4, 50),
                Conjured("Conjured Mana Cake", 2, 4)
                ]

items_day_nine = [NormalItem("+5 Dexterity Vest", 1, 2),
                AgedBrie("Aged Brie", -7, 16),
                NormalItem("Elixir of the Mongoose", -4, 0),
                Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80),
                Sulfuras("Sulfuras, Hand of Ragnaros", -1, 80),
                Backstage("Backstage passes to a TAFKAL80ETC concert", 6, 33),
                Backstage("Backstage passes to a TAFKAL80ETC concert", 1, 50),
                Backstage("Backstage passes to a TAFKAL80ETC concert", -4, 0),
                Conjured("Conjured Mana Cake", -6, 0)
                ]

items_day_nineteen = [NormalItem("+5 Dexterity Vest", -9, 0),
                AgedBrie("Aged Brie", -17, 36),
                NormalItem("Elixir of the Mongoose", -14, 0),
                Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80),
                Sulfuras("Sulfuras, Hand of Ragnaros", -1, 80),
                Backstage("Backstage passes to a TAFKAL80ETC concert", -4, 0),
                Backstage("Backstage passes to a TAFKAL80ETC concert", -9, 0),
                Backstage("Backstage passes to a TAFKAL80ETC concert", -14, 0),
                Conjured("Conjured Mana Cake", -16, 0)
                ]

items_day_thirty = [NormalItem("+5 Dexterity Vest", -20, 0),
                AgedBrie("Aged Brie", -28, 50),
                NormalItem("Elixir of the Mongoose", -25, 0),
                Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80),
                Sulfuras("Sulfuras, Hand of Ragnaros", -1, 80),
                Backstage("Backstage passes to a TAFKAL80ETC concert", -15, 0),
                Backstage("Backstage passes to a TAFKAL80ETC concert", -20, 0),
                Backstage("Backstage passes to a TAFKAL80ETC concert", -25, 0),
                Conjured("Conjured Mana Cake", -27, 0)
                ]