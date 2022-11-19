![Copy of MDA II Final Presentation (2)](https://user-images.githubusercontent.com/103318089/202837294-8c740113-641e-40cd-bfc4-f335cfdb2798.png)




&nbsp;

<!-- About the Project -->
# :star2: About the Project

PlanIt* is a prototype project engineered to ingest data from Spotify and Twitter, analyze it, and make forecasts of music trends (artists and songs) that are valuable to festival planners and music touring industry based on the current demand.

The tool analyzes the music taste of an audience and identify artists and songs that could tailor best a music gig. 

As a result, PlanIt* creates recommendations for opening acts based on featured artist selection and playlists


<!-- TechStack -->
# :space_invader: Tech Stack

Here's a brief high-level overview of the tech stack the project uses:

- For the ingestion platform, we leverage [NIFI](https://nifi.apache.org/), for both streaming and batch ingestion from our data sources Spotify and Twitter.
- The project uses the [HDFS](https://hadoop.apache.org/docs/r1.2.1/hdfs_design.html) as our primary storage system
- Processing layer leverage mainly [Apache Spark](https://spark.apache.org/). We leverage also ML and Graphframes for advance analytics
- Our serving layer is made of [MariaDB](https://fonts.google.com/specimen/Work+Sans) for data base storage
- Finally, analytics done with [Power BI](https://powerbi.microsoft.com/en-cy/). POC Dashboard can be visualized here [PlanIt Dashboard](https://app.powerbi.com/view?r=eyJrIjoiYTFhNzhhMDItYTBhMy00NzRjLThlNDItYmQwOWViYjVjMzFkIiwidCI6IjczNDU4NDQzLTE2MjctNDA5MS04YjM5LTIyMjIxMzQ5MDdjNSIsImMiOjh9&pageName=ReportSection)

![MDA II Final Presentation](https://user-images.githubusercontent.com/103318089/201260606-1be77a42-c03b-48bc-8ec8-58336f0ca7d4.png)

<!-- Features -->
# :dart: Features

- By ingesting data from the [Spotify API](https://developer.spotify.com/documentation/web-api/) we combine and rank a selection of artists by analyzing top charts, frequency of appearance, followers and popularity and generate reccommendations relevant to tour managers, festival organizers to support their decision making.
- We leverage [Spotify API](https://developer.spotify.com/documentation/web-api/) and [Twitter](https://developer.twitter.com/en/docs/twitter-api) to better understand popularity trends and social media positioning of music artists.
- We generate recommendations for young bands to open for larger, more established performers as supporting acts based on song's audio features similarities and social media trends.
- Leverage fan's music taste in order to identiy the best song line-up for concerts and music events.

# :bookmark_tabs: Documentation

You can find our documentation [here](https://github.com/Callisthenes/music_industry_intelligence/documentation) with the following tutorials

- Update Nifi: Updates done in the course environment that allowed us to stream ingest from Twitter leveraging NIFI processor. 
- Spotify Config Ingestion: Step by step guidance of Spotify Ingestion leveraging Postman.
- Tweepy tutorial: Step by step guidance on how to ingest from twitter leveraging Tweepy.
- Two objects working with our VM environment: Sharing a workaround to be able to work with 2 os.environment on the same Jupyter notebook which allowed us to work both with Graphframes and Mariadb.
- Connect Powerbi to vm: Step by step guidance on how to connect the course environment to PowerBi and leverage the full potential of dashboard analytics

# ✨ Contributors 

Thanks goes to these wonderful people

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/domro11"><img src="https://avatars.githubusercontent.com/u/108944195?v=4" width="100px;" alt="Dominik Roser"/><br /><sub><b>Dominik Roser</b></sub></a><br /><a href="https://github.com/codesandbox/codesandbox-client/commits?author=NinoMaj" title="Documentation">💻</a></td>
    <td align="center"><a href="https://github.com/CarlosBlazquezP"><img src="https://avatars.githubusercontent.com/u/108976036?v=4" width="100px;" alt="Carlos Blazquez"/><br /><sub><b>Carlos Blazquez</b></sub></a><br /><a href="https://github.com/codesandbox/codesandbox-client/commits?author=saurabhdaware" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/dianisley"><img src="https://avatars.githubusercontent.com/u/103318089?v=4" width="100px;" alt="Diana Fernandez"/><br /><sub><b>Diana Fernandez</b></sub></a><br /><a href="https://github.com/codesandbox/codesandbox-client/commits?author=pablopunk" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/CBRodulfo"><img src="https://avatars.githubusercontent.com/u/107241015?v=4" width="100px;" alt="Christian Barba"/><br /><sub><b>Christian Barba</b></sub></a><br /><a href="https://github.com/codesandbox/codesandbox-client/commits?author=ryanpwaldon" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/hibashanaa"><img src="https://avatars.githubusercontent.com/u/15159069?v=4" width="100px;" alt="Hiba Shanaa"/><br /><sub><b>Hiba Shanaa</b></sub></a><br /><a href="https://github.com/codesandbox/codesandbox-client/commits?author=cherniavskii" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/markantoinehourany"><img src="https://avatars.githubusercontent.com/u/108943228?v=4" width="100px;" alt="Mark Hourany"/><br /><sub><b>Mark Hourany</b></sub></a><br /><a href="https://github.com/codesandbox/codesandbox-client/commits?author=NullVoxPopuli" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/Callisthenes"><img src="https://avatars.githubusercontent.com/u/91435423?v=4" width="100px;" alt="Pedro V. Esteban"/><br /><sub><b>Pedro V. Esteban</b></sub></a><br /><a href="https://github.com/codesandbox/codesandbox-client/issues?q=author%3Aaditya211935" title="Bug reports">💻</a></td> 
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->


