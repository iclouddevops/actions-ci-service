package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func HandlerPing(ctx *gin.Context) {
	// return data object hello
	ctx.JSON(http.StatusOK, gin.H{
		"code":    0,
		"message": "pong",
	})
}

func main() {
	// hello world
	r := gin.Default()

	r.GET("/ping", HandlerPing)

	r.Run() // listen and serve on 0.0.0.0:8080
}
