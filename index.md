---
layout: default
---

<div class="container index-container">
    <div class="row">
         <div class="col s6 in-progress-div">
            <div class="in-progress">IN PROGRESS</div>
            <div class="desc-menu">Work in progress on GitHub</div>
            <ul>
            {%  for post in site.posts %}
                {% if post.tag == "wip" %}
                <li class="post-title-li"><a class="post-title" href="{{post.url | prepend:site.baseurl }}" > {{ post.title }}</a></li>
                {% endif %}
            {% endfor %}
            </ul>
        </div>
        
        <div class="col s6 complete-div">
            <ul>
            {%  for post in site.posts %}
                {% if post.tag != "wip" %}
                <li class="post-title-li"><a class="post-title" href="{{post.url | prepend:site.baseurl }}" > {{ post.title }}</a></li>
                {% endif %}
            {% endfor %}
            </ul>
        </div>
        
    </div>
</div>

<style>
    .in-progress{
        font-weight: 800;
        letter-spacing: 0.1em;
        text-indent:0.2em;
        font-size: 1.2em;
    }
    .index-container{
        margin-top: 3em;
    }
    .post-title{
        color: black;
        border-bottom: 1px dotted black;
    }
    .post-title:hover{
        background: lightgrey;
    }
    .post-title-li{
        padding-bottom: 0.5em;
    }
    .in-progress-div{
        border-right: 1px lightgrey solid;
    }
    .complete-div{
        text-align: right;
    }
</style>
