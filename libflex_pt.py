def flexCategory(data):
    content = {
        "type": "bubble",
        "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "image",
                        "url": str(data['images']),
                        "size": "full",
                        "aspectMode": "cover",
                        "aspectRatio": "3:4",
                        "gravity": "top"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": str(data['name']),
                                        "size": "xl",
                                        "color": "#ffffff",
                                        "weight": "bold"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "PT BURN&COOK  RESTAURANT",
                                        "color": "#FF764B",
                                        "size": "xs",
                                        "flex": 0,
                                        "weight": "bold"
                                    }
                                ],
                                "spacing": "lg"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "button",
                                        "action": {
                                            "type": "message",
                                            "label": "ดูเมนู",
                                            "text": str(data['name']),
                                        },
                                        "color": "#ebebeb",
                                        "gravity": "center",
                                        "position": "relative",
                                        "height": "sm",
                                        "offsetBottom": "3px"
                                    }
                                ],
                                "borderColor": "#FF764B",
                                "cornerRadius": "6px",
                                "borderWidth": "1px",
                                "height": "30px",
                                "position": "relative",
                                "margin": "20px"
                            }
                        ],
                        "position": "absolute",
                        "offsetBottom": "0px",
                        "offsetStart": "0px",
                        "offsetEnd": "0px",
                        "backgroundColor": "#271F1F",
                        "paddingAll": "20px",
                        "paddingTop": "18px"
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                            {
                                "type": "icon",
                                "url": "https://scontent.xx.fbcdn.net/v/t1.15752-9/p206x206/241520489_840873460125872_4470261117295722616_n.png?_nc_cat=111&ccb=1-5&_nc_sid=aee45a&_nc_eui2=AeGAnJuB2PnQmL6rcEDprIzpOg57bHm2MFo6DntsebYwWiryhqKW2IWlPClP1RBLrqNiXp5COLXIN8YC5Lkp5STZ&_nc_ohc=m3LxZzrjgQEAX81Jzbe&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=01e3559a8529e0f8f77d27187c0be917&oe=616EC294",
                                "size": "4xl",
                                "position": "relative"
                            },
                            {
                                "type": "icon",
                                "url": "https://scontent.xx.fbcdn.net/v/t1.15752-9/cp0/241405376_1930832140417976_5448961625846663346_n.png?_nc_cat=105&ccb=1-5&_nc_sid=aee45a&_nc_eui2=AeH9qrSXA548obQcU_wVW7pWOUSnm0AtxvA5RKebQC3G8MAbK5gyUelSjHmTo3QuQc7Mxv89c62W90K8vkHPOdoh&_nc_ohc=XuuaFf4kC5AAX_4pwJw&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=734e9698109f498a659fe1136510e1f2&oe=616ED90C",
                                "offsetEnd": "4px",
                                "offsetTop": "-15px"
                            },
                            {
                                "type": "icon",
                                "url": "https://scontent.xx.fbcdn.net/v/t1.15752-9/cp0/241405376_1930832140417976_5448961625846663346_n.png?_nc_cat=105&ccb=1-5&_nc_sid=aee45a&_nc_eui2=AeH9qrSXA548obQcU_wVW7pWOUSnm0AtxvA5RKebQC3G8MAbK5gyUelSjHmTo3QuQc7Mxv89c62W90K8vkHPOdoh&_nc_ohc=XuuaFf4kC5AAX_4pwJw&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=734e9698109f498a659fe1136510e1f2&oe=616ED90C",
                                "offsetEnd": "4px",
                                "offsetTop": "-15px"
                            }
                        ],
                        "position": "absolute",
                        "borderColor": "#FF764B",
                        "borderWidth": "2px",
                        "cornerRadius": "60px",
                        "height": "50px",
                        "backgroundColor": "#ED2E3F",
                        "offsetStart": "220px",
                        "offsetTop": "280px",
                        "width": "100px"
                    }
                ],
            "paddingAll": "0px"
        }
    }
    return content


def flexProduct(data):
    content = {
        "type": "bubble",
        "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "image",
                        "url": str(data['images']),
                        "size": "full",
                        "aspectMode": "cover",
                        "aspectRatio": "3:4",
                        "gravity": "top"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": str(data['name']),
                                        "size": "xl",
                                        "color": "#ffffff",
                                        "weight": "bold"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": str(data['description']),
                                        "color": "#FF764B",
                                        "size": "sm",
                                        "flex": 0,
                                        "weight": "bold"
                                    }
                                ],
                                "spacing": "lg"
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": str(data['price']),
                                        "color": "#ebebeb"
                                    },
                                    {
                                        "type": "text",
                                        "text": "บาท/จาน",
                                        "position": "absolute",
                                        "offsetStart": "30px",
                                        "color": "#FF764B",
                                        "weight": "bold"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "button",
                                        "action": {
                                            "type": "message",
                                            "label": "สั่งอาหาร",
                                            "text": str(data['name']),
                                        },
                                        "color": "#ebebeb",
                                        "gravity": "center",
                                        "position": "relative",
                                        "height": "sm",
                                        "offsetBottom": "5px"
                                    }
                                ],
                                "borderColor": "#FF764B",
                                "cornerRadius": "6px",
                                "borderWidth": "1px",
                                "height": "30px",
                                "position": "relative",
                                "margin": "20px"
                            }
                        ],
                        "position": "absolute",
                        "offsetBottom": "0px",
                        "offsetStart": "0px",
                        "offsetEnd": "0px",
                        "backgroundColor": "#271F1F",
                        "paddingAll": "20px",
                        "paddingTop": "18px"
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                            {
                                "type": "icon",
                                "url": "https://scontent.xx.fbcdn.net/v/t1.15752-9/p206x206/241520489_840873460125872_4470261117295722616_n.png?_nc_cat=111&ccb=1-5&_nc_sid=aee45a&_nc_eui2=AeGAnJuB2PnQmL6rcEDprIzpOg57bHm2MFo6DntsebYwWiryhqKW2IWlPClP1RBLrqNiXp5COLXIN8YC5Lkp5STZ&_nc_ohc=m3LxZzrjgQEAX81Jzbe&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=01e3559a8529e0f8f77d27187c0be917&oe=616EC294",
                                "size": "4xl",
                                "position": "relative"
                            },
                            {
                                "type": "icon",
                                "url": "https://scontent.xx.fbcdn.net/v/t1.15752-9/cp0/241405376_1930832140417976_5448961625846663346_n.png?_nc_cat=105&ccb=1-5&_nc_sid=aee45a&_nc_eui2=AeH9qrSXA548obQcU_wVW7pWOUSnm0AtxvA5RKebQC3G8MAbK5gyUelSjHmTo3QuQc7Mxv89c62W90K8vkHPOdoh&_nc_ohc=XuuaFf4kC5AAX_4pwJw&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=734e9698109f498a659fe1136510e1f2&oe=616ED90C",
                                "offsetTop": "-15px",
                                "offsetEnd": "4px"
                            },
                            {
                                "type": "icon",
                                "url": "https://scontent.xx.fbcdn.net/v/t1.15752-9/cp0/241405376_1930832140417976_5448961625846663346_n.png?_nc_cat=105&ccb=1-5&_nc_sid=aee45a&_nc_eui2=AeH9qrSXA548obQcU_wVW7pWOUSnm0AtxvA5RKebQC3G8MAbK5gyUelSjHmTo3QuQc7Mxv89c62W90K8vkHPOdoh&_nc_ohc=XuuaFf4kC5AAX_4pwJw&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=734e9698109f498a659fe1136510e1f2&oe=616ED90C",
                                "offsetTop": "-15px",
                                "offsetEnd": "4px"
                            }
                        ],
                        "position": "absolute",
                        "borderColor": "#FF764B",
                        "borderWidth": "2px",
                        "cornerRadius": "60px",
                        "height": "50px",
                        "backgroundColor": "#ED2E3F",
                        "offsetStart": "220px",
                        "offsetTop": "260px",
                        "width": "100px"
                    }
                ],
            "paddingAll": "0px"
        }
    }
    return content


def flexCart_product_whitdel(data):
    content = {
        "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "text",
                        "text": str(data['name']),
                        "size": "sm",
                        "color": "#ffffff",
                        "flex": 4
                    },
                    {
                        "type": "text",
                        "text": "x" + str(data['qty']),
                        "size": "sm",
                        "color": "#FF764B",
                        "align": "end",
                        "flex": 1
                    },
                    {
                        "type": "text",
                        "text": str(f"{data['total']:,}"),
                        "size": "sm",
                        "color": "#FF764B",
                        "align": "end",
                        "flex": 1
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                            {
                                "type": "icon",
                                "url": "https://scontent.xx.fbcdn.net/v/t1.15752-9/p206x206/61625382_450342892381616_9025235832461590528_n.png?_nc_cat=111&ccb=1-5&_nc_sid=aee45a&_nc_eui2=AeGyi9aMRZhhuZ_UZ_EDcviZFMM477K_jaMUwzjvsr-No1wT5WRxZvuORAr5CSyKJrY61yvZ_Gn6UieXCw97wJO4&_nc_ohc=tzbloonPJu8AX9FmBfd&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=cad2d369442678173d0e10406f7724a6&oe=61755B2A"
                            }
                        ],
                        "alignItems": "center",
                        "justifyContent": "center",
                        "action": {
                            "type": "message",
                            "label": "action",
                            "text": "ลบสินค้า : " + str(data['name']),
                        }
                    }
                ]
    }
    return content


def flexCart_product(data):
    content = {
        "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "text",
                        "text": str(data['name']),
                        "size": "sm",
                        "color": "#ffffff",
                        "flex": 4
                    },
                    {
                        "type": "text",
                        "text": "x" + str(data['qty']),
                        "size": "sm",
                        "color": "#FF764B",
                        "align": "end",
                        "flex": 1
                    },
                    {
                        "type": "text",
                        "text": str(f"{data['total']:,}"),
                        "size": "sm",
                        "color": "#FF764B",
                        "align": "end",
                        "flex": 1
                    }
                ]
    }
    return content


def flexCart(data, detail):
    content = {
        "type": "bubble",
        "size": "giga",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "ตระกร้าสินค้า",
                    "weight": "bold",
                    "color": "#FF764B",
                    "size": "sm"
                },
                {
                    "type": "text",
                    "text": str(data['date']),
                    "size": "xs",
                    "color": "#ffffff",
                    "wrap": True
                },
                {
                    "type": "text",
                    "text": str(data['lineId']),
                    "size": "xs",
                    "color": "#1DB446",
                    "wrap": True
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "xxl",
                    "spacing": "sm",
                    "contents": detail
                },
                {
                    "type": "separator",
                    "margin": "xl",
                    "color": "#FF764B"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "xs",
                    "spacing": "xs",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "margin": "xxl",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "ITEMS",
                                    "size": "sm",
                                    "color": "#ffffff"
                                },
                                {
                                    "type": "text",
                                    "text": str(data['items']),
                                    "size": "sm",
                                    "color": "#FF764B",
                                    "align": "end"
                                }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "total",
                                    "size": "sm",
                                    "color": "#ffffff"
                                },
                                {
                                    "type": "text",
                                    "text":  str(f"{data['total']:,}"),
                                    "size": "sm",
                                    "color": "#FF764B",
                                    "align": "end"
                                }
                            ]
                        }
                    ]
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "margin": "md",
                    "contents": [
                        {
                            "type": "icon",
                            "url": "https://scontent.xx.fbcdn.net/v/t1.15752-9/p206x206/242393089_4008742272564557_8092279073413223390_n.png?_nc_cat=108&ccb=1-5&_nc_sid=aee45a&_nc_eui2=AeFj6ZUJ00D3tftsNecwiJghgiU0dGZWV-WCJTR0ZlZX5dSnsnrXKgpn2MYBBiFmCTUHXfz1bpdKFkDprQ8oGKXk&_nc_ohc=TrmXnuApnzUAX-gkbmT&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=d48b43c709ac0ea664c9d04312973549&oe=616F890F",
                            "size": "4xl",
                            "position": "relative"
                        }
                    ],
                    "position": "absolute",
                    "width": "200px",
                    "height": "50px",
                    "backgroundColor": "#271F1F",
                    "borderWidth": "2px",
                    "borderColor": "#FF764B",
                    "cornerRadius": "60px",
                    "offsetStart": "220px",
                    "offsetTop": "20px"
                }
            ],
            "backgroundColor": "#271F1F"
        }
    }
    return content


def flexResult(data):
    content = {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "ตะกร้าสินค้า",
                    "weight": "bold",
                    "color": "#FF764B",
                    "size": "xl"
                },
                {
                    "type": "text",
                    "text": "PT BURN&COOK  RESTAURANT",
                    "weight": "bold",
                    "size": "xs",
                    "margin": "md",
                    "color": "#ffffff"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "xxl",
                    "spacing": "sm",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "Energy Drink",
                                    "size": "sm",
                                    "color": "#ffffff",
                                    "flex": 0
                                },
                                {
                                    "type": "text",
                                    "text": "$2.99",
                                    "size": "sm",
                                    "color": "#FF764B",
                                    "align": "end"
                                }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "Chewing Gum",
                                    "size": "sm",
                                    "color": "#ffffff",
                                    "flex": 0
                                },
                                {
                                    "type": "text",
                                    "text": "$0.99",
                                    "size": "sm",
                                    "color": "#FF764B",
                                    "align": "end"
                                }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "Bottled Water",
                                    "size": "sm",
                                    "color": "#ffffff",
                                    "flex": 0
                                },
                                {
                                    "type": "text",
                                    "text": "$3.33",
                                    "size": "sm",
                                    "color": "#FF764B",
                                    "align": "end"
                                }
                            ]
                        },
                        {
                            "type": "separator",
                            "margin": "xxl",
                            "color": "#FF764B"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "margin": "xxl",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "ITEMS",
                                    "size": "sm",
                                    "color": "#ffffff"
                                },
                                {
                                    "type": "text",
                                    "text": "3",
                                    "size": "sm",
                                    "color": "#FF764B",
                                    "align": "end"
                                }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "TOTAL",
                                    "size": "sm",
                                    "color": "#ffffff"
                                },
                                {
                                    "type": "text",
                                    "text": "$7.31",
                                    "size": "sm",
                                    "color": "#FF764B",
                                    "align": "end"
                                }
                            ]
                        }
                    ]
                },
                {
                    "type": "separator",
                    "margin": "xxl",
                    "color": "#FF764B"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "margin": "md",
                    "contents": [
                        {
                            "type": "icon",
                            "url": "https://scontent.xx.fbcdn.net/v/t1.15752-9/p206x206/242393089_4008742272564557_8092279073413223390_n.png?_nc_cat=108&ccb=1-5&_nc_sid=aee45a&_nc_eui2=AeFj6ZUJ00D3tftsNecwiJghgiU0dGZWV-WCJTR0ZlZX5dSnsnrXKgpn2MYBBiFmCTUHXfz1bpdKFkDprQ8oGKXk&_nc_ohc=TrmXnuApnzUAX-gkbmT&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=d48b43c709ac0ea664c9d04312973549&oe=616F890F",
                            "size": "4xl",
                            "position": "relative"
                        }
                    ],
                    "position": "absolute",
                    "height": "50px",
                    "backgroundColor": "#271F1F",
                    "borderWidth": "2px",
                    "borderColor": "#FF764B",
                    "cornerRadius": "60px",
                    "offsetStart": "220px",
                    "offsetTop": "40px"
                }
            ],
            "backgroundColor": "#271F1F"
        },
        "styles": {
            "footer": {
                "separator": True
            }
        }
    }
    return content


