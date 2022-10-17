from discord_webhook import DiscordWebhook
import time
import random
from random import randint


nums = [1,2,3,4,5,6,7,8,9,10]

webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1028018503543967764/wW1j0p3G0MpWvZmbzb2YW4-CGtDN4A152wH_2aYwnV-QS405JzLZaww84Zfa566iKI8F", content=f'{nums}')

i = 0 
while i < len(nums):
    response = webhook.execute()
    webhook.content = f'{nums}'
    if "\u274C" in nums:
        nums.remove("\u274C")
    nums[random.randint(0, len(nums)-1)] = "\u274C"
    time.sleep(3)
    response = webhook.edit(response)

