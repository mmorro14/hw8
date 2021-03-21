function runSearch(term) {
	// hide and clear the previous results, if any
	$("#results").hide()
	$("tbody").empty()

	// transforms all the form parameters into a string we can send to the server
	var frmStr = $("#gene_search").serialize()

	$.ajax({
		url: "./search_genes.cgi",
		dataType: "json",
		data: frmStr,
		success: function (data, textStatus, jqXHR) {
			processJSON(data)
		},
		error: function (jqXHR, textStatus, errorThrown) {
			alert("Failed to perform gene search! textStatus: (" + textStatus + ") and errorThrown: (" + errorThrown + ")")
		},
	})
}

function clickedSearch(data) {
	$("#gene_search").alert(data)
	$("#results").show()
}

function alertMessage(hours, msg, hours) {
	var hoursPerDay = hours
	var hello = "There are " + hours + " hours per day: Dumb " + msg

	// this writes content to the browser window
	hello.appendTo("h1")
	// this adds content to a pop-up window
	alert(hello)
}

// this processes a passed JSON structure representing gene matches and draws it
//  to the result table
function processJSON(data) {
	// set the span that lists the match count
	$("#match_count").text(data.match_count)

	// this will be used to keep track of row identifiers
	var next_row_num = 1

	// iterate over each match and add a row to the result table for each
	$.each(data.matches, function (i, item) {
		var this_row_id = "result_row_" + next_row_num++

		// create a row and append it to the body of the table
		$("<tr/>", { id: this_row_id }).appendTo("tbody")

		// add the locus column
		$("<td/>", { text: item.locus_id }).appendTo("#" + this_row_id)

		// add the product column
		$("<td/>", { text: item.product }).appendTo("#" + this_row_id)
	})

	// now show the result section that was previously hidden
	$("#results").show()
}

// run our javascript once the page is ready
$(document).ready(function () {
	// define what should happen when a user clicks submit on our search form
	$("#submit").click(function () {
		$("#gene_search").text(data.gene_search)
		runSearch()
		return false // prevents 'normal' form submission
	})
})

$("#autocomplete").autocomplete({
	lookup: function (query, done) {
		// Do Ajax call or lookup locally, when done,
		// call the callback and pass your results:
		var result = {
			suggestions: [
				{ value: "United Arab Emirates", data: "AE" },
				{ value: "United Kingdom", data: "UK" },
				{ value: "United States", data: "US" },
			],
		}

		done(result)
	},
	onSelect: function (suggestion) {
		alert("You selected: " + suggestion.value + ", " + suggestion.data)
	},
})
