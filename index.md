---
layout: page
title: Home
order: 1
permalink: /
---

<div class="container index-container">
    <div class="row">        
        <div class="col s12 complete-div parent-wrapper">
            <div class="post-parent">
                {% for tag in site.categories %} 
                {% if tag[0] != 'implementation' %}
                <div class="post-child">
                  <h4 id="{{ tag[0] }}" class="">{{ tag[0] | capitalize }}</h4>
                  <ul class="post-list">
                    {% assign pages_list = tag[1] %}  
                    {% for post in pages_list %}
                    {% if post.title != null %}
                    {% if group == null or group == post.group %}
                    <li class="post-title-li"><a class="post-title" href="{{post.url | prepend:site.baseurl }}" > {{ post.title }}</a></li>
                    {% endif %}
                    {% endif %}
                    {% endfor %}
                    {% assign pages_list = nil %}
                    {% assign group = nil %}
                </ul>
            </div>
            {% endif %}
            {% endfor %}
        </div>
    </div>   
</div>
</div>

<style type="text/css">
    .parent-wrapper {
        height:100%;
    }
    .post-parent {
        display: flex;
        font-size: 0;
        font-size: 1em;
        flex-wrap:wrap;
        margin:-10px 0 0 -10px;
    }
    .post-parent li:hover{
        cursor: pointer;
    }
    .post-child {
        display: inline-block;
        margin:10px 0 0 10px;
        flex-grow: 1;
        width: calc(100% * (1/4) - 10px - 1px);
        margin: 0.5em;
    }

    .index-container {
        margin-top: 3em;
        text-align: center;
    }
    @media only screen and (min-width: 993px){
        .container {
            width: 90%;
        }
    }
</style>
