# CalendarAvailability
This algorithm takes two lists. The first entry in each list is that person's bounds for when they are GENERALLY avaliable/awake in a day (for example, 8:00AM-5:00PM).
The rest of the entires in each list are meetings that each person has already scheduled, and therefore cannot meet during these times.
This algorithm takes these lists, along with a minimum meeing length, and returns all the possible times those two people could have a meeting that day.
