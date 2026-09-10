#!/bin/bash
set -e
cd "$(dirname "$0")/.."

FILMS_DIR="assets/images/films"
PHOTO_DIR="assets/images/photography"

declare -A FILMS=(
  ["big-sister.jpg"]="https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/1742845921400-URA2AGVNOO3ZF46MSU5M/BigSister02_Thumbnail.jpg"
  ["trapped.jpg"]="https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/6e886193-60d3-491e-868e-da20ba492e96/Trapped_Thumbnail.jpg"
  ["bunny-ears.png"]="https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/1742847953182-Z0NNSHRK9IDY4PB0C6CU/BunnyEars.png"
  ["pink-razor.jpg"]="https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/1742847818196-H92OMRF26SIZ467WG9XI/BackToSchool_PinkRazor%20%281%29.jpg"
  ["shopper-thoughts.png"]="https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/1742846796705-1A2MGEPCFA4D4U4YEH56/ShopperThoughts.png"
  ["cart-star.jpg"]="https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/1742846979818-8UDP7YRGQXP4FQ3I633C/Shoppers_Thumbnails.jpg"
  ["back-to-school.png"]="https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/1742847069335-YEMH47DTJHRT88SYXI13/DealWeek.png"
  ["tell-your-story.png"]="https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/1742847160816-3MLPFI3QWZPFA8MRA5W4/Steven.png"
)

for name in "${!FILMS[@]}"; do
  curl -sL "${FILMS[$name]}" -o "$FILMS_DIR/$name"
  echo "downloaded $name"
done

PHOTOS=(
  "https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/2e649e50-bc71-42c8-9a83-464d097a8956/%EF%BF%BC%EF%BF%BC20220224_Chelsea-Kyle_InstaCart_02_Glitzy-GIF_TAKE-07_102_R1.jpg"
  "https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/c3454061-dc75-4d0f-8c76-c59d72dd3d00/%EF%BF%BC%EF%BF%BC20220224_Chelsea-Kyle_InstaCart_03_Hipster-GIF-2_TAKE-08_021_R1.jpg"
  "https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/2819dc90-c49a-4af9-9183-123178f39a1c/%EF%BF%BC%EF%BF%BC20220224_Chelsea-Kyle_InstaCart_04_food-nerd-GIF_TAKE-02_107_R1.jpg"
  "https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/b968148c-6193-4115-b8ba-085f24bc71a9/%EF%BF%BC%EF%BF%BC20220224_Chelsea-Kyle_InstaCart_01_Jokester-GIF-2_TAKE-07_023_R1.jpg"
  "https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/5e5de1d0-44c1-44c4-90f0-da6781398805/032222_Product_Comms0551.jpg"
  "https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/86f6cb38-e806-4920-91ad-f9681ded9a98/032222_Product_Comms0783.jpg"
  "https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/a6432ebf-ba74-44f0-a8c8-93148f95d87a/Vintage---Portrait_042922_Alcohol-Growth0101_FINAL.gif"
  "https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/bd582066-3a8b-4fd6-be8a-64dd39d73f6f/Chill_Surfer_Portrait-Wide_042922_Alcohol_Growth0990.jpg"
  "https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/1610410e-5c0a-442a-b689-06f3d3fd7972/YDK-Portrait_Wide_042822_Alcohol_Growth1626.jpg"
  "https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/fa6921a7-3b0a-4cb7-933a-f8c2a79cfe33/Portait-Tight-SOFIA_042722_Alcohol-Growth2983.gif"
  "https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/377ef935-02eb-457f-912e-dfe0f204152a/DIY-Hands_042822_Alcohol_Growth2750.jpg"
  "https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/ce782790-8f98-451b-a73e-9e2dc73a5b7e/092022_Oct_Merch_4824_Craveable_Candy.jpg"
  "https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/4d640cd6-3985-4c33-94b2-6ca2706075b6/092022_Oct_Merch_4836_Delicious_Colors.jpg"
  "https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/0448cff9-0090-4b30-8253-d3b96ad28f37/Macro_Sofia_042822_Alcohol_Growth0608.jpg"
  "https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/05c4bf46-d5a1-48e7-a207-17f6c4c55325/Macro_Floral_Cocktail_042922_Alcohol_Growth3268.jpg"
  "https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/c4b35165-e109-4d42-a7f2-75715836a7e5/032522_Cinco_De_Mayo_V2.jpg"
  "https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/4b03ccc4-b07b-4c00-a6f6-8d20eb0f4289/032522_Cinco-De-Mayo_1346GIF_1200x1200_7x.gif"
  "https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/ab8c2339-4a8c-4640-bf46-ba83b8f69ff5/041122_CPS_Mothers_Day_0684.jpg"
  "https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/0a7519d3-c5e2-489b-a701-42b58d8f4f79/041222_CPS_Mothers_Day_1056.jpg"
  "https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/72d39c32-ac93-46be-b8d1-d8ba8d44acf6/041222_CPS_Mothers_Day_1377.jpg"
  "https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/aa8801d2-1a3d-4d57-a8d3-c54f6cbda324/031022_Spring_Beauty_0125_Final.jpg"
  "https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/e07dec9b-fa81-4b65-976e-4466a450a67b/SHOTA-1_BENTO_ALCOHOL_GENERAL-LIVINGROOM_WIDE_SHOT_0614-v2.jpg"
  "https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/b6ab7efa-a4b1-419c-994e-652d475bd996/SHOTBSC-1_BEAUTY_SELF_CARE-BATH-WIDE_SHOT_3517-v2.jpg"
  "https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/331e22b4-fb36-46b9-8e31-6352a208fdcd/092022_Oct_Merch_gif_Cozy_SoupGIF.gif"
  "https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/17ced5ca-9649-4200-b476-0eda95798857/092022_Oct_Merch_4768_Fall_Flavors.jpg"
  "https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/999ad396-9f56-4d1e-88bf-4128f867e692/CAR_03_01460_JinxFinal.jpg"
  "https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/3effc97a-75e3-47a3-8eee-2c5433657d73/GROCERY_DROP_OFF_01_03566_JinxFinal.jpg"
  "https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/04167e9c-66b8-4a8b-b666-33b26c634c70/GROCERY_DROP_OFF_02_00238_JinxFinal.jpg"
  "https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/d4184974-b606-4308-bc31-234513b7e91e/PRODUCE_04_05058_yellow_JinxFinal.jpg"
  "https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/512948f4-7680-49f3-b32d-b5d01fa1af84/GROCERY_DROP_OFF_07_01102_JinxFinal.jpg"
  "https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/51f62e3f-6804-433a-aed5-f3c87300322a/KENYA_LOADING_GROCERIES_02306_JinxFinal.jpg"
  "https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/7dc2f335-ee00-4a7c-b68c-e34baaed9b40/KENYA_LOADING_GROCERIES_MAIN_HOUSE_KITCHEN_01_03363.jpg"
  "https://images.squarespace-cdn.com/content/v1/63b08823c6b0c8363c7ea4f3/d463d343-f79c-4c9b-8485-71291c9f19e8/KITCHEN_04_01842-_JinxFinal.jpg"
)

i=1
for url in "${PHOTOS[@]}"; do
  ext="${url##*.}"
  ext="${ext%%\?*}"
  num=$(printf "%02d" $i)
  curl -sL "$url" -o "$PHOTO_DIR/photo-$num.$ext"
  echo "downloaded photo-$num.$ext"
  i=$((i+1))
done

echo "All assets downloaded."
