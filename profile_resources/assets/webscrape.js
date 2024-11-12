const axios = require('axios');
const cheerio = require('cheerio');
const fs = require('fs');

// Base URL for the category page
const baseUrl = 'https://en.wikipedia.org/wiki/Category:Given_names';

let allNames = [];

// Function to scrape a single page and handle pagination
async function scrapePage(url) {
  try {
    const { data } = await axios.get(url);
    const $ = cheerio.load(data);

    // Extract names from the page (all links under `.mw-category-group a`)
    $('.mw-category-group a').each((i, elem) => {
      const name = $(elem).text();
      allNames.push(name);
    });

    // Check for the "next page" link and scrape the next page if it exists
    const nextPageLink = $('a:contains("next page")').attr('href');
    if (nextPageLink) {
      // Recursively scrape the next page
      await scrapePage(`https://en.wikipedia.org${nextPageLink}`);
    }
  } catch (error) {
    console.error('Error fetching the page:', error);
  }
}

// Main function to start the scraping and save results
async function main() {
  console.log("Starting scraping...");
  
  // Start scraping from the initial page
  await scrapePage(`${baseUrl}?from=Aa`);

  // Remove duplicates if needed
  allNames = [...new Set(allNames)];

  // Save all names to a text file
  fs.writeFileSync('given_names.txt', allNames.join('\n'), 'utf-8');
  console.log(`Scraping complete! ${allNames.length} names saved to given_names.txt`);
}

// Run the main function
main();
