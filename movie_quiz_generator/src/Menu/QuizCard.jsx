import * as React from "react";
import Box from "@mui/material/Box";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import Typography from "@mui/material/Typography";
import { CardMedia, CardActionArea } from "@mui/material";

export default function QuizCard(props) {
  const { subject, description, imagePath } = props;

  const handleConfig = () => {
    props.updateQuizData((prevState) => ({
      ...prevState,
      subject: subject,
      config: true,
    }));
  };

  return (
    <Box sx={{ minWidth: 180 }}>
      <Card variant="outlined">
        <CardActionArea>
          <CardMedia
            component="img"
            height="300"
            image={imagePath}
            alt={subject}
            onClick={handleConfig}
          />
          <CardContent>
            <Typography gutterBottom variant="h5" component="div">
              {subject}
            </Typography>
            <Typography variant="body2" color="text.secondary">
              {description}
            </Typography>
          </CardContent>
        </CardActionArea>
      </Card>
    </Box>
  );
}
