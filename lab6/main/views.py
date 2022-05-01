from django.http import HttpResponse

from main.classes.MusicStoreDatabaseManager import MusicStoreDataBaseManager

styles = """
<style>
    body {
        font-family: arial, sans-serif;
        width: 500px;
        margin: auto;
    }

    h3 {
        text-align: center;
    }

    table {
        border-collapse: collapse;
        width: 100%;
    }

    thead tr {
        background-color: aquamarine;
    }

    td, th {
        border: 1px solid #dddddd;
        text-align: left;
        padding: 8px;
    }

    tr:nth-child(even) {
        background-color: #dddddd;
    }
</style>
"""

manager = MusicStoreDataBaseManager()


def author_to_html(author_id: int, name: str):
    return """
    <tr>
        <td>%s</td>
        <td>%s</td>
        <td><a href="albums/%s">%s</a></td>
    </tr>""" % (author_id, name, author_id, name)


def album_to_html(album_id: int, name: str, number_of_songs: int, author_id: int):
    return """
    <tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
    </tr>""" % (album_id, name, number_of_songs, author_id)


def authors(request):
    author_list, _ = manager.get_all_authors()
    return HttpResponse("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Authors</title>
        %s
    </head>
    <body>
        <h3>Authors</h3>
        <table>
            <thead>
                <tr>
                    <th>Author id</th>
                    <th>Name</th>
                    <th>Link to albums<th>
                </tr>
            </thead>
            <tbody>
            %s
            </tbody>
        </table>
    </body>
    </html>
""" % (styles, ''.join([author_to_html(p[0], p[1]) for p in author_list])))


def albums(request, author_id):
    album_list, _ = manager.find_album_by_condition("author_id", author_id, "*")
    return HttpResponse("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Albums</title>
        %s
    </head>
    <body>
        <h3>Albums</h3>
        <table>
            <thead>
                <tr>
                    <th>Album id</th>
                    <th>Name of album</th>
                    <th>Number of songs</th>
                    <th>Author id</th>
                </tr>
            </thead>
            <tbody>
            %s
            </tbody>
        </table>
    </body>
    </html>
""" % (styles, ''.join([album_to_html(v[0], v[1], v[2], v[3]) for v in album_list])))
