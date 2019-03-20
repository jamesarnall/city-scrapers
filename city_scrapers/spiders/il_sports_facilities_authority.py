from city_scrapers_core.constants import NOT_CLASSIFIED
from city_scrapers_core.items import Meeting
from city_scrapers_core.spiders import CityScrapersSpider
from dateutil.parser import parse
import re


class IlSportsFacilitiesAuthoritySpider(CityScrapersSpider):
    name = "il_sports_facilities_authority"
    agency = "Illinois Sports Facilities Authority"
    timezone = "America/Chicago"
    allowed_domains = ["www.isfauthority.com"]
    start_urls = ["https://www.isfauthority.com/governance/board-meetings/"]

    def parse(self, response):
        """
        `parse` should always `yield` Meeting items.

        Change the `_parse_id`, `_parse_name`, etc methods to fit your scraping
        needs.
        """

        para_text = self._get_paragraph_of_meetings(response.css('h2:contains("Meetings and Agendas") ~ p'))
        listings = self._get_meetings_from_paragraph(para_text)


        for listing in listings:
            meeting = self._parse_meeting(listing)
            yield meeting

    def _parse_title(self, itemTxt):
        """Parse or generate meeting title."""
        # ^(\w|\s)+
        return re.match(r'^(\w|\s)+(?=\s\d{1,2}.\d{1,2}.\d{4})', itemTxt).group()

    def _parse_date(self, itemTxt):
        date_str = re.findall(r'([\d]{1,2}.[\d]{1,2}.[\d]{4})', itemTxt)[0]
        out_date = parse(date_str)
        return out_date
        # ([\d]{1,2}.[\d]{1,2}.[\d]{4})

    def _parse_description(self, item):
        """Parse or generate meeting description."""
        return ""

    def _parse_classification(self, item):
        """Parse or generate classification from allowed options."""
        return NOT_CLASSIFIED

    def _parse_start(self, txt):
        """Parse start datetime as a naive datetime object."""
        return self._parse_date(txt)

    def _parse_end(self, item):
        """Parse end datetime as a naive datetime object. Added by pipeline if None"""
        return None

    def _parse_time_notes(self, item):
        """Parse any additional notes on the timing of the meeting"""
        return ""

    def _parse_all_day(self, item):
        """Parse or generate all-day status. Defaults to False."""
        return False

    def _parse_location(self, item):
        """Parse or generate location."""
        return {
            "address": "",
            "name": "",
        }

    def _parse_links(self, item):
        """Parse or generate links."""
        return [{"href": "", "title": ""}]

    def _parse_source(self, response):
        """Parse or generate source."""
        return response.url

    # 
    # Pulls text for the <p> containing the list of meetings
    def _get_paragraph_of_meetings(self, response):
        listings = response.css('h2:contains("Meetings and Agendas") ~ p').getall()
        para = listings[1].replace('<p>', '').replace('</p>', '')
        return para

    #
    # Parses paragraph text and returns a list of HTML strings defining each meeting
    def _get_meetings_from_paragraph(self, txt):
        lines_of_text = txt.replace('<br>', '')
        return lines_of_text.split('\n')
        
    def _parse_meeting(self, txt):
        data = {
            'title': self._parse_title(txt),            
            'start': self._parse_start(txt)
        }
        return data
        
            # meeting = Meeting(
            #     title          = self._parse_title(item),
            #     description    = self._parse_description(item),
            #     classification = self._parse_classification(item),
            #     start          = self._parse_start(item),
            #     end            = self._parse_end(item),
            #     all_day        = self._parse_all_day(item),
            #     time_notes     = self._parse_time_notes(item),
            #     location       = self._parse_location(item),
            #     links          = self._parse_links(item),
            #     source         = self._parse_source(response),
            # )

            # meeting["status"] = self._get_status(meeting)
            # meeting["id"] = self._get_id(meeting)

