window.onload = function () {
	console.log("onload started")
	$("#gene_search").autocomplete({
		source: "search_product.cgi",
	})
	$("#students").autocomplete({
		source: "search_product.cgi",
		minLength: 2,
		select: function (event, ui) {
			// enter a function here to do once the user selects something
		},
		html: true,
	})
}
// getSource
var source = $("#gene_search").autocomplete("option", "source")

// setSource
$(".selector").autocomplete("option", "source", function () {})

$(".selector").autocomplete({
	search: function (event, ui) {},
})
