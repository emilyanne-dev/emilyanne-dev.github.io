#!/bin/bash
set -e
cd "$(dirname "$0")/.."

FILMS_DIR="assets/images/films"

NAMES=(
  "big-sister.jpg"
  "trapped.jpg"
  "bunny-ears.png"
  "pink-razor.jpg"
  "shopper-thoughts.png"
  "cart-star.jpg"
  "back-to-school.png"
  "tell-your-story.png"
)

URLS=(
  "https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/1742845921400-URA2AGVNOO3ZF46MSU5M/BigSister02_Thumbnail.jpg"
  "https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/6e886193-60d3-491e-868e-da20ba492e96/Trapped_Thumbnail.jpg"
  "https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/1742847953182-Z0NNSHRK9IDY4PB0C6CU/BunnyEars.png"
  "https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/1742847818196-H92OMRF26SIZ467WG9XI/BackToSchool_PinkRazor%20%281%29.jpg"
  "https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/1742846796705-1A2MGEPCFA4D4U4YEH56/ShopperThoughts.png"
  "https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/1742846979818-8UDP7YRGQXP4FQ3I633C/Shoppers_Thumbnails.jpg"
  "https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/1742847069335-YEMH47DTJHRT88SYXI13/DealWeek.png"
  "https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/1742847160816-3MLPFI3QWZPFA8MRA5W4/Steven.png"
)

for i in "${!NAMES[@]}"; do
  curl -sL "${URLS[$i]}" -o "$FILMS_DIR/${NAMES[$i]}"
  echo "downloaded ${NAMES[$i]}"
done

echo "Films downloaded."
